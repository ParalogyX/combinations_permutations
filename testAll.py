# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:04:22 2021

@author: vpe
"""

import combperm

#If tst = 1 only digitList
#If tst = 2 only stringList
#If tst = 3 - both

tst = 1

if tst in (1,3): 
    digitList = list(range(10))
stringList = 'abcdefhg'

if tst in (1,3): 
    digitCode = combperm.combinaionsAndPermutations(digitList)
if tst in (2,3): 
    stringCode = combperm.combinaionsAndPermutations(stringList)

for i in range(1,5):
    print(i)
    if tst in (1,3): 
        digitCode.SetTypeOfCombination(i)
    if tst in (2,3): 
        stringCode.SetTypeOfCombination(i)
    if tst in (1,3): 
        print("Digital code type:", digitCode.GetTypeOfCombination())
    if tst in (2,3): 
        print("String code type:", stringCode.GetTypeOfCombination())
    if tst in (1,3):
        for j in range (1, digitCode.GetAmountOfElements() + 1):
            digitCode.SetItemsInCombination(j)
            print("Digital code of", digitCode.GetItemsInCombination(), 
                                   "digits have ", digitCode.AmountOfCombinations(), "combinations")
            
    if tst in (2,3):
        for j in range (1, stringCode.GetAmountOfElements() + 1):
            stringCode.SetItemsInCombination(j)

            print("String code of", stringCode.GetItemsInCombination(), 
                                   "symbols have", stringCode.AmountOfCombinations(), "combinations")
            
            
       
            
