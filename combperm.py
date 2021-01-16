# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:36:21 2021

Functions to calculate combinaions and permutations

@author: vpe
"""

#TODO: input check (both int, n > 0, 0 < r <= n)

#TODO: add class, where you can load list of objects and add methods to show all combinations
#       Current functions also add to the class

def factorial(n):
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
    return factorial

def CombinationWithRepetition(n, r):
    """
    Calculates amount of combinations of r in n variables with repetition is possible
    E.g n=4 (1,2,3,4), r=2, variants:
    11
    12
    13
    14
    22
    23
    24
    33
    34
    44    
    
    Order doesn't matter!!! 21 = 12
    
    Parameters
    ----------
    n : int
        Amount of different types.
    r : int
        Amount of selected types.

    Returns
    -------
    int
        Amount of combinations.

    """
    return int(factorial(n+r-1)/(factorial(r) * factorial(n-1)))



def CombinationWithoutRepetition(n, r):
    """
    Calculates amount of combinations of r in n variables without repetition is possible
    E.g n=4 (1,2,3,4), r=2, variants:
    12
    13
    14
    23
    24
    34    
    
    Order doesn't matter!!! 21 = 12
    
    Parameters
    ----------
    n : int
        Amount of different types.
    r : int
        Amount of selected types.

    Returns
    -------
    int
        Amount of combinations.

    """
    return int(factorial(n)/(factorial(r) * factorial(n-r)))


def PermutationWithRepetition(n, r):
    """
    Calculates amount of permutaions of r in n variables with repetition is possible
    E.g n=4 (1,2,3,4), r=2, variants:
    11
    12
    13
    14
    21
    22
    23
    24
    31
    32
    33
    34
    41
    42
    43
    44    
    
    Order does matter!!! 21 != 12
    
    Parameters
    ----------
    n : int
        Amount of different types.
    r : int
        Amount of selected types.

    Returns
    -------
    int
        Amount of permutaions.

    """
    return int(n**r)



def PermutationWithoutRepetition(n, r):
    """
    Calculates amount of permutaions of r in n variables without repetition is possible
    E.g n=4 (1,2,3,4), r=2, variants:
    12
    13
    14
    21
    23
    24
    31
    32
    34
    41
    42
    43      
    
    Order does matter!!! 21 != 12
    
    Parameters
    ----------
    n : int
        Amount of different types.
    r : int
        Amount of selected types.

    Returns
    -------
    int
        Amount of combinations.

    """
    return int(factorial(n)/factorial(n-r))