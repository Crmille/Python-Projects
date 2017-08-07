# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:08:07 2017

@author: Chad-PC
"""

def getDPR():
    apr_input = float(input("Current APR: "))
    dpr = apr_input / 360
    return dpr

def getAVD():
    continueCounter = 1
    average_daily_balance = 0
    
    while continueCounter:
        print("Item:",continueCounter)
        itemCost = float(input("Cost of item: "))
        itemDuration = float(input("Duration of item: "))
        
        if itemDuration > 30:
            itemDuration = 30
            
        if itemDuration < 1:
            print("An item's Duration must be longer than 1 day.")
            continue
        
        if itemCost < 0:
            print("An item's cost must be larger than 0.")
            continue
        
        
        average_daily_balance += itemCost * itemDuration
        
        continueCounter = continueCounter+1        
        continueFlag = input("Continue? y/n: ")
        continueFlag = continueFlag.lower()
        if continueFlag == 'y':
            continue
        else: break
    
    
    return average_daily_balance

def main():
    print("APR Calculator")
    adb = getAVD()
    dpr = getDPR()
    
    creditInterest = adb * dpr
    
    print(creditInterest)
    return creditInterest   
    

if __name__== "__main__":
    main()