#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:31:57 2018

@author: zhangxinrun
"""

'''
        Below are the three functions which I defined in this program
'''
from copy import deepcopy
#For using the deepcopy() function, I have to import the copy library
#I searched on the Internet to find the function to copy a dictionary
#finally I found it, below is the Website
#https://www.cnblogs.com/mokero/p/6662202.html

def DisplayTheGrades(newGrades):
    #This function is to display the grades in different subjects for each student.
    #input: newGrades(dict)
    #output: information(string)
    print("student" + "  ECE595" + "  ECE547" + "  ECE354\n")
    #print the first line of display
    for foo in newGrades:
        print(str(foo).ljust(7) + str(newGrades[foo][0]).rjust(5) + str(newGrades[foo][1]).rjust(8) + str(newGrades[foo][2]).rjust(9))
    #print newGrades.
    #ljust() and rjust() are used to adjust the position of outputs, 
    #which makes it easier to read
    #this is the website which these functions come from
    #http://www.runoob.com/python/att-string-rjust.html


def DisplayTheHighest(Grades):
    #This function is to display the highest score and scorer in each subject.
    #input: Grades(dict)
    #output: information(string,highest score and its scorer)
    print("Please select a course:")
    choice = int(input("1.ECE595 2.ECE547 3.ECE354\n"))
    choice -= 1
    #user chooses the course he want
    temp1 = 0
    temp2 = ""
    #temp1 stores the score
    #temp2 stores the name
    for foo in Grades:
        if int(Grades[foo][choice]) > temp1:
            temp1 = int(Grades[foo][choice])
            temp2 = foo
    #finding the highest score and its scorer
    print("The highest score in this course is: " + str(temp1))
    print("Its scorer is: " + temp2)
    
    
def DisplayTheGPA(Grades, newGrades):
    #This function is to display the GPA of each student.
    #The credit hours for each course is 3 
    #and points for A, B, C, D, and F are 4, 3, 2, 1, and 0, respectively.
    #input: Grades(dict)
    #output: information(string)
    tempGrades = deepcopy(newGrades)
    #This dict is uded to store each student's credit for each course
    n = 0
    for foo in tempGrades:
        while n<3:
            if tempGrades[foo][n] == 'A':
                tempGrades[foo][n] = 12
                n += 1
            elif tempGrades[foo][n] == 'B':
                tempGrades[foo][n] = 9
                n += 1
            elif tempGrades[foo][n] == 'C':
                tempGrades[foo][n] = 6
                n += 1
            elif tempGrades[foo][n] == 'D':
                tempGrades[foo][n] = 3
                n += 1
            else:
                tempGrades[foo][n] = 0
                n += 1
        n = 0
    #change "A""B""C" into credits 12,9,6...
    print("student" + "   GPA")
    for foo in tempGrades:
        key = foo
        value = round((int(tempGrades[foo][0]) + int(tempGrades[foo][1]) + int(tempGrades[foo][2])) / 9, 2)
        print(str(key).ljust(7) + str(value).rjust(7))
    #Calculate the GPA and print it
    #functions which are used are same as function1
        


'''
        Below is the code which shows how to get the data from the file
        and put them into two new dictionaries (Grades and newGrades)
'''
print("Loading...")
#Open the file and get the data, put them into a dictionary.
Grades = {}
#Set an empty dict.
try:
    openFile = open('records.txt','r')
    #open the file 'records.txt'
    for line in openFile:
        if line != '\n':
            index = line.find(',')
            key = line[:index]  
            value = line[index+1:-1]
            Grades[key] = value
            #firstly, if line isn't empty, slice the line into two parts
            #first part is the name(str)
            #second part is the grades(str)
            #In this function I refer to the following website：
            #https://blog.csdn.net/rooki_men/article/details/52088300
    for grades in Grades:
        Grades[grades] = Grades[grades].split(",") 
        #turned grades(str) into grades(tuple)
        #The function split() can seperate string by specified separator and put them into a tuple
        #this can convennient the operation later            
finally:
    if openFile:
        openFile.close()
    #now the file can be closed

Grades.pop('student')
#delete the first line

n = 0
#n is used to count the int number in tuple
newGrades = deepcopy(Grades)
#deepcopy the Grades to genurate a new dict named newGrades
#this movement is important to protect the origin data in Grades
for foo in newGrades:
    while n < 3:
        if int(newGrades[foo][n]) >= 90:
            newGrades[foo][n] = 'A'
            n += 1
        elif int(newGrades[foo][n]) >= 80 and int(newGrades[foo][n]) <= 89:
            newGrades[foo][n] = 'B'
            n += 1
        elif int(newGrades[foo][n]) >= 70 and int(newGrades[foo][n]) <= 79:
            newGrades[foo][n] = 'C'
            n += 1
        elif int(newGrades[foo][n]) >= 60 and int(newGrades[foo][n]) <= 69:
            newGrades[foo][n] = 'D'
            n += 1
        elif int(newGrades[foo][n]) <59:
            newGrades[foo][n] = 'F'
            n += 1
    n = 0
    #replace int grades with 'A''B''C'...in newGrades(dict)



'''
        Below is the main code of this program
        including welcome displaying and function choices
'''
#print(Grades)
#print(newGrades)
#Delete the "#" to print the Grades and newGrades(dictionaries) to check out thier structure

print("Welcome to ZXR's Grade system...")
print("What can I do for you?")
#print a welcome:)
while 1:
    command = int(input("Please input the number:\n1. Display the grades\n2. Display the highest score and scorer in each subject\n3. Display the GPA of each student.\n4. Quit the program\n"))
    if command == 1:
        DisplayTheGrades(newGrades)
    elif command == 2:
        DisplayTheHighest(Grades)
    elif command == 3:
        DisplayTheGPA(Grades, newGrades)
    elif command == 4:
        print("Thank you for using!")
        print("Goodbye!")
        break
    else:
        print("I don't understand. Pleas try again!")

'''
The functions which I build in this program are still can be improved.
The difficulties of this task mainly concentrate on how to find
a proper and handy structure to store and handle the data
There must be better solutions on the Internet.
Peace :)
'''