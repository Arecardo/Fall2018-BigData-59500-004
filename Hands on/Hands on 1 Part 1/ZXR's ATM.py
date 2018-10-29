#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 14:47:47 2018

@author: zhangxinrun
"""

print("Welcome to ZXR Bank's ATM Machine!")
print("We have bills for 100$, 50$, 20$, 10$, and 5$!")
#Print a welcome, be nice man:)
bills = {'$100':0,' $50':0,' $20':0,' $10':0,'  $5':0}
#Define a dictionary to store the amount of bills
#I put blanks before the key for sake of beauty :)
while 1:
    #It's convennient to test the program if I put it in an infinity loop
    withDrawal = int(input("Enter the amount for withdrawal:"))
    #Get the input number from client
    if withDrawal%5 != 0:
        print("The amount cannot be withdrawn.")
    #If withdrawal cannot be divisible by 5, print the error.
    else:
        bills['$100'] = withDrawal//100
        withDrawal -= bills['$100']*100

        bills[' $50'] = withDrawal//50
        withDrawal -= bills[' $50']*50
        
        bills[' $20'] = withDrawal//20
        withDrawal -= bills[' $20']*20
        
        bills[' $10'] = withDrawal//10
        withDrawal -= bills[' $10']*10

        bills['  $5'] = withDrawal//5
        withDrawal -= bills['  $5']*5
        #Calculate the number of bills, put them into dictionary
        #First divide the withDrawwal by 100, get the quotient, 
        #then subtract the already calculated part, divide it again by 50, 
        #get the quotient, then subtract, and so on.
        #I dont think it's an efficent way :(, but I figure it out by myself :)
    for dollar in bills:
        if bills[dollar] != 0:
            print(dollar + ':' + str(bills[dollar]))
        #Now we get the answer 
        #This loop is used to traverse the dictionary
        #If key != 0, output it
        