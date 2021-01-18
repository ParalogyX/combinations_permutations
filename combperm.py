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
        """
        Initialization of combinaionsAndPermutations.

        Parameters
        ----------
        collection : list, tuple, str or dict
            Not empty iterable collection of items used for combinations.
        typeOfCombination : 1, 2, 3 or 4, optional
            1 - Combination With Repetition.
            2 - Combination Without Repetition.
            3 - Permutation With Repetition.
            4 - Permutation Without Repetition. The default is 1.
        r : positive int, optional
            Amount of items in combination. The default is 1.

        Raises
        ------
        RuntimeError
            If collection is not iterable, or typeOfCombination is not 1, 2, 3 or 4, 
            or r is more than lenght of collection, generates RuntimeError "Wrong arguments".

        Returns
        -------
        None.

        """
            
        if (type (collection) not in (list, tuple, str, dict) or 
            typeOfCombination not in (1,2,3,4) or 
            not 0 < r <= len(collection)):
                raise RuntimeError("Wrong arguments")
            
        self.collection = collection
        self.typeOfCombination = typeOfCombination
        self.r = r
        self.n = len(collection)
        
    def SetCollection(self, collection):
        """
        Update a collecion. Automatically decreases Amount of items in combination (r) 
        in case current value is bigger, than collection lenght

        Parameters
        ----------
        collection : Not empty list, tuple, str or dict
            Iterable collection of items used for combinations.

        Raises
        ------
        RuntimeError
            If collection is not iterable generates RuntimeError "Wrong arguments".

        Returns
        -------
        None.

        """
        if type (collection) not in (list, tuple, str, dict):
            raise RuntimeError("Wrong arguments")
        self.collection = collection
        self.n = len(collection)
        if self.r > self.n:
            self.r = self.n
        
    def SetTypeOfCombination(self, typeOfCombination):
        """
        Update type of combination

        Parameters
        ----------
        typeOfCombination : 1, 2, 3 or 4.
            1 - Combination With Repetition.
            2 - Combination Without Repetition.
            3 - Permutation With Repetition.
            4 - Permutation Without Repetition.

        Raises
        ------
        RuntimeError
            If typeOfCombination is not 1, 2, 3 or 4 generates RuntimeError "Wrong arguments".

        Returns
        -------
        None.

        """
        if typeOfCombination not in (1,2,3,4):
            raise RuntimeError("Wrong arguments")
        self.typeOfCombination = typeOfCombination
        
    def SetItemsInCombination(self, r):
        """
        Update amount of items in combination

        Parameters
        ----------
        r : positive int
            Amount of items in combination..

        Raises
        ------
        RuntimeError
            If r is more than lenght of collection, generates RuntimeError "Wrong arguments".

        Returns
        -------
        None.

        """
        if not 0 < r <= len(self.collection):
            raise RuntimeError("Wrong arguments")
        self.r = r

    def GetCollection(self):
        """
        Returns collection

        Returns
        -------
        list, tuple, str or dict.
            Current collection of items.

        """
        return self.collection

    def GetTypeOfCombination(self):
        """
        Returns name of type of combination
        1 - Combination With Repetition.
        2 - Combination Without Repetition.
        3 - Permutation With Repetition.
        4 - Permutation Without Repetition.

        Returns
        -------
        str
            Type of combination.

        """
        option = {1: "Combination With Repetition", 2: "Combination Without Repetition",
                  3: "Permutation With Repetition", 4: "Permutation Without Repetition"}
        return option[self.typeOfCombination]
    
    def GetItemsInCombination(self):
        """

        Returns
        -------
        int
            Amount of items in combination.

        """
        return self.r
    
    def GetAmountOfElements(self):
        """
        

        Returns
        -------
        int
            Lenght of collection.

        """
        return self.n
    
    
    def AmountOfCombinations(self):
        """
        Calculates amount of all possible combinations of selected type

        Returns
        -------
        int
            Amount of combinations.

        """
        option = {1: CombinationWithRepetition, 2: CombinationWithoutRepetition,
                  3: PermutationWithRepetition, 4: PermutationWithoutRepetition}
        return option[self.typeOfCombination](self.n, self.r)
        
    def AllCombinations(self, maxLines = 10):
        """
        Returns list of all possible combinatios of selected type, limited by maxLines.
        WARNING: Large maxLines (more than ~10000000) can cause memory issues and freezing.
                 Always check AmountOfCombinations() before and setup good maxLines.

        Parameters
        ----------
        maxLines : int, optional
            Limitation of output. The default is 10.

        Returns
        -------
        result : list
            First maxLines of all possible combinations.

        """

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