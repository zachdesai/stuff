#! /usr/bin/python3
from math import floor

def returnOrdValue(char):
    if char.isupper():
        res = ord(char) - 38
    elif char.islower():
        res = ord(char) - 96
    return res


with open('./input.txt','r') as file:
    input=file.readlines()
    dupeList = []
    grouper = []
    commonItemsList = []

    for line in input:
        # Question 1
        line.strip()
        #print(line)
        a = line[:floor((len(line)/2))]
        #print(a)
        b = line[floor((len(line)/2)):]
        #print(b)
        for char in a:
            if char in b:
                #print("appending " + char)
                dupeList.append(char)
                break

        # Question 2

        if len(grouper) < 3:
            grouper.append(line.strip())
            print("appending " + line + " to grouper")
        elif len(grouper) == 3:
            print(grouper)
            for char in grouper[0]:
                if char in grouper[1]:
                    print(char + " in common")
                    if char in grouper[2]:
                        print(char + " in common 2")
                        commonItemsList.append(char)
                        grouper = []
                        grouper.append(line.strip())
                        break
    # Because of some logic issues, the last set of elves is not calculated in the loop
    # quick hack to do the last calculation
    for char in grouper[0]:
        if char in grouper[1]:
            print(char + " in common")
            if char in grouper[2]:
                print(char + " in common 2")
                commonItemsList.append(char)
                grouper = []
                grouper.append(line.strip())
                break
    question_1 = 0
    question_2 = 0


    for dupe in dupeList:
        question_1 += returnOrdValue(dupe)
    print(commonItemsList)
    for common in commonItemsList:
        question_2 += returnOrdValue(common)
    print(question_1)
    print(question_2)
    
# Uppercase ord shift for A-Z=27-52
# A=65   65-27=38
# lowercase ord shift a-z=1-26
# a=97 97-1 = 96