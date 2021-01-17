# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:36:21 2021

Functions to calculate combinaions and permutations

@author: vpe
"""
import itertools


def factorial(n):
    """
    Calculates factorial of n

    Parameters
    ----------
    n : int
        Positive integer.

    Returns
    -------
    factorial : int
        Factorial of n.

    """
    if n < 0 or type(n) != int:
        raise RuntimeError("Wrong arguments")
    
    factorial = 1
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i
    return factorial

class combinaionsAndPermutations(object):
    
    
    
    def __init__(self, collection, typeOfCombination = 1, r = 1):
            
        if (type (collection) not in (list, tuple, str, dict) or 
            typeOfCombination not in (1,2,3,4) or 
            not 0 < r <= len(collection)):
                raise RuntimeError("Wrong arguments")
            
        self.collection = collection
        self.typeOfCombination = typeOfCombination
        self.r = r
        self.n = len(collection)
        
    def SetCollection(self, collection):
        if type (collection) not in (list, tuple, str, dict):
            raise RuntimeError("Wrong arguments")
        self.collection = collection
        self.n = len(collection)
        if self.r > self.n:
            self.r = self.n
        
    def SetTypeOfCombination(self, typeOfCombination):
        if typeOfCombination not in (1,2,3,4):
            raise RuntimeError("Wrong arguments")
        self.typeOfCombination = typeOfCombination
        
    def SetItemsInCombination(self, r):
        if not 0 < r <= len(self.collection):
            raise RuntimeError("Wrong arguments")
        self.r = r

    def GetCollection(self):
        return self.collection

    def GetTypeOfCombination(self):
        option = {1: "Combination With Repetition", 2: "Combination Without Repetition",
                  3: "Permutation With Repetition", 4: "Permutation Without Repetition"}
        return option[self.typeOfCombination]
    
    def GetItemsInCombination(self):
        return self.r
    
    def GetAmountOfElements(self):
        return self.n
    
    
    def AmountOfCombinations(self):
        option = {1: CombinationWithRepetition, 2: CombinationWithoutRepetition,
                  3: PermutationWithRepetition, 4: PermutationWithoutRepetition}
        return option[self.typeOfCombination](self.n, self.r)
        
    def AllCombinations(self, maxLines = 10):
        
        # if (self.AmountOfCombinations() > 100 and not MoreThanHundred):
        #     print ("Too many combinations (> 100). You need to call function\
        #            AmountOfCombinations with parameter MoreThanHundred = True")
        #     return []
        
        # if self.AmountOfCombinations() > 10000 and safety:
        #     print ("Too many combinations (> 10000). Risk of freezing!!!. You need to call function AmountOfCombinations with parameter safety = False.")
        #     return
        option = {1: itertools.combinations_with_replacement, 2: itertools.combinations,
                  3: itertools.product, 4: itertools.permutations}
        
        result = []
        i = 0
        if self.typeOfCombination == 3:
            for comb in itertools.product(self.collection, repeat = self.r):
                result.append(comb)
                i += 1
                if i >= maxLines:
                    break
        else:
            for comb in option[self.typeOfCombination](self.collection, self.r):
                result.append(comb)
                i += 1
                if i >= maxLines:
                    break
        return result

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
        Amount of different types. Positive integer.
    r : int
        Amount of selected types. Positive integer, less or equal n.

    Returns
    -------
    int
        Amount of combinations.

    """
    
    if type(n) != int or type(r) != int or (n <= 0) or not 0 < r <= n:
        raise RuntimeError("Wrong arguments")
    
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
        Amount of different types. Positive integer.
    r : int
        Amount of selected types. Positive integer, less or equal n.

    Returns
    -------
    int
        Amount of combinations.

    """
    if type(n) != int or type(r) != int or (n <= 0) or not 0 < r <= n:
        raise RuntimeError("Wrong arguments")
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
        Amount of different types. Positive integer.
    r : int
        Amount of selected types. Positive integer, less or equal n.

    Returns
    -------
    int
        Amount of permutaions.

    """
    if type(n) != int or type(r) != int or (n <= 0) or not 0 < r <= n:
        raise RuntimeError("Wrong arguments")
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
        Amount of different types. Positive integer.
    r : int
        Amount of selected types. Positive integer, less or equal n.

    Returns
    -------
    int
        Amount of combinations.

    """
    if type(n) != int or type(r) != int or (n <= 0) or not 0 < r <= n:
        raise RuntimeError("Wrong arguments")
    return int(factorial(n)/factorial(n-r))