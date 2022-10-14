"""Linked lists."""

from __future__ import annotations
from os import access
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar('T')


@dataclass
class L(Generic[T]):
    """
    A single link in a linked list.

    The `head` attribute gives you the value at the head of
    this list while `tail` gives you the rest of the list,
    or None if the rest is the empty list.

    >>> L(1, L(2, L(3, None)))
    L(1, L(2, L(3, None)))
    """

    head: T
    tail: List[T]

    def __repr__(self) -> str:
        """Representation of this object."""
        return f"L({self.head}, {self.tail})"


List = Optional[L[T]]  # A list is an L() constructor or None


# Direct recursive versions ###########################################


def length(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length(None)
    0
    >>> length(L(1, None))
    1
    >>> length(L(1, L(2, L(3, None))))
    3
    """
    return 0 if x is None else 1 + length(x.tail)


def add(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add(None)
    0
    >>> add(L(1, None))
    1
    >>> add(L(1, L(2, L(3, None))))
    6
    """
    return 0 if x is None else x.head + add(x.tail)


def contains(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains(L(1, L(2, L(3, None))), 4)
    False
    >>> contains(L(1, L(2, L(3, None))), 2)
    True
    """
    ...
    if x == None: 
        return False 
    if e == x.head: 
        return True 
    elif x.tail != None:
        return contains(x.tail, e)
    else:
        return False


#print(contains(L(1, L(2, L(3, None))), 2))
#print(contains(L(1, L(2, L(3, None))), 4))





def drop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop(x, 3)
    L(4, None)
    """
    if x == None: 
        return x 
    if k == 0: 
        return x
    else:
        return drop(x.tail, k-1)

#print(drop(L(1, L(2, L(3, L(4, None)))), 0))
#print(drop(L(1, L(2, L(3, L(4, None)))), 1))
#print(drop(L(1, L(2, L(3, L(4, None)))), 3))


def keep(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep(x, 0) # returns None but doesn't print
    >>> keep(x, 1)
    L(1, None)
    >>> keep(x, 3)
    L(1, L(2, L(3, None)))
    """
    if x == None:
        return None
    if k == 0: 
        return None
    else: 
        return L(x.head,keep(x.tail, k-1)) 


#print(keep(L(1, L(2, L(3, L(4, None)))), 1))
#print(keep(L(1, L(2, L(3, L(4, None)))), 3))




def concat(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """

    if x == None:
        return y 
    else:
        return L(x.head, concat(x.tail, y))
        
#print(concat(L(1, L(2, None)), L(3, L(4, None))))



def append(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    k = length(x)

    if x == None: 
        return L(e, None) 
    else: 
        return L(x.head,append(x.tail, e)) 

#print(append(L(1, L(2, None)), 3))



def rev(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    ...

    if x == None:
        return None
    return append(rev(x.tail), x.head)


#print(rev(L(1, L(2, L(3, None)))))




# Tail-recursive versions ###########################################


def length_tr(x: List[T], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> length_tr(None)
    0
    >>> length_tr(L(1, None))
    1
    >>> length_tr(L(1, L(2, L(3, None))))
    3
    """
    return acc if x is None else length_tr(x.tail, acc + 1)


def add_tr(x: List[int], acc: int = 0) -> int:
    """
    Compute the length of x.

    >>> add_tr(None)
    0
    >>> add_tr(L(1, None))
    1
    >>> add_tr(L(1, L(2, L(3, None))))
    6
    """
    return acc if x is None else add_tr(x.tail, acc + x.head)


def contains_tr(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_tr(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_tr(L(1, L(2, L(3, None))), 2)
    True
    """
    
    if x == None: 
        return False 
    if e == x.head: 
        return True
    return contains_tr(x.tail, e)


#print(contains_tr(L(1, L(2, L(3, None))), 4))
#print(contains_tr(L(1, L(2, L(3, None))), 2))


def drop_tr(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_tr(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_tr(x, 3)
    L(4, None)
    """
    
    if k == 0: 
        return x
    else:
        return drop_tr(x.tail, k-1)

#print(drop_tr(L(1, L(2, L(3, L(4, None)))), 0))
#print(drop_tr(L(1, L(2, L(3, L(4, None)))), 1))
#print(drop_tr(L(1, L(2, L(3, L(4, None)))), 3))



def keep_tr(x: List[T], k: int, acc: List[T] = None) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep_tr(x, 0) # returns None but doesn't print
    >>> keep_tr(x, 1)
    L(1, None)
    >>> keep_tr(x, 3)
    L(1, L(2, L(3, None)))
    """
    if x == None:
        return rev(acc)
    if k != None:
        if k == 0: 
            return rev(acc)
        else: 
            return keep_tr(x.tail, k-1, L(x.head, acc)) 


#print(keep_tr(L(1, L(2, L(3, L(4, None)))), 1))
#print(keep_tr(L(1, L(2, L(3, L(4, None)))), 3))


def flip(x: List[T], y: List[T]) -> List[T]:

    if y == None:
        return x 
    return flip(L(y.head, x), y.tail)

#print(flip(L(3, L(4, None)), L(2, L(1, L(0, None)))))




def concat_tr(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_tr(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    return flip(y, rev(x))

#print(concat_tr(L(1, L(2, None)), L(3, L(4, None))))


def append_tr(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append_tr(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat_tr(x, L(e, None))

#print(append_tr(L(1, L(2, None)), 3))

def rev_tr(x: List[T], acc: List[T]=None) -> List[T]:
    """
    Reverse a list.

    >>> rev_tr(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    if x == None:
        return acc
    return rev_tr(x.tail, L(x.head, acc))

#print(rev_tr(L(1, L(2, L(3, None)))))



# Loop versions ###########################################

def length_loop(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length_loop(None)
    0
    >>> length_loop(L(1, None))
    1
    >>> length_loop(L(1, L(2, L(3, None))))
    3
    """
    acc = 0
    while x:
        acc += 1
        x = x.tail
    return acc


def add_loop(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> add_loop(None)
    0
    >>> add_loop(L(1, None))
    1
    >>> add_loop(L(1, L(2, L(3, None))))
    6
    """
    acc = 0
    while x:
        acc += x.head
        x = x.tail
    return acc


def contains_loop(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains_loop(L(1, L(2, L(3, None))), 4)
    False
    >>> contains_loop(L(1, L(2, L(3, None))), 2)
    True
    """
    
    while x:
        if e == x.head:
            return True
        else: 
            x = x.tail
    else: 
        return False 


def drop_loop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop_loop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop_loop(x, 3)
    L(4, None)
    """
    
    while x: 
        if k == 0:
            return x 
        else: 
            x = x.tail
            k -= 1 

#print(drop_loop(L(1, L(2, L(3, L(4, None)))), 3)) 


def keep_loop(x: List[T], k: int, acc: List[T] = None) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep_loop(x, 0) # returns None but doesn't print
    >>> keep_loop(x, 1)
    L(1, None)
    >>> keep_loop(x, 3)
    L(1, L(2, L(3, None)))
    """
    while True: 
        if x == None:
            return rev_tr(acc)
        if k == 0: 
            return rev_tr(acc)
        x, k, acc = x.tail, k-1, L(x.head, acc)
    

print(keep_loop(L(1, L(2, L(3, L(4, None)))), 1))
print(keep_loop(L(1, L(2, L(3, L(4, None)))), 3))


def flip_loop(x: List[T], y: List[T]) -> List[T]:
    
    while True: 
        if y == None: 
            return x
        x, y = L(y.head, x), y.tail

#print(flip_loop(L(3, L(4, None)), L(2, L(1, L(0, None)))))

def concat_loop(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat_loop(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    return flip_loop(y,rev(x))

#print(concat_loop(L(1, L(2, None)), L(3, L(4, None))))


def append_loop(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append_loop(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat_loop(x, L(e, None))

#print(append_loop(L(1, L(2, None)), 3))

def rev_loop(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev_loop(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    return flip_loop(None, x)

#print(rev_loop(L(1, L(2, L(3, None)))))
