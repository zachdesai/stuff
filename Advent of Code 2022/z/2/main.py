#! /usr/bin/python3

# x rock, y paper, z scissors
# a rock, b paper, c scissors
# loss 0, draw 3, win 6
# x rock +1, y paper +2, z scissors +3
# x loss, y draw, z win

def returnWinnersScore(theirRoll, myRoll):
    if theirRoll == "A":
        if myRoll == "X":
            return 3
        elif myRoll == "Y":
            return 6
        elif myRoll == "Z":
            return 0
    elif theirRoll == "B":
        if myRoll == "X":
            return 0
        elif myRoll == "Y":
            return 3
        elif myRoll == "Z":
            return 6
    elif theirRoll == "C":
        if myRoll == "X":
            return 6
        elif myRoll == "Y":
            return 0
        elif myRoll == "Z":
            return 3

def returnMyRollScore(myRoll):
        if myRoll == "X":
            return 1
        elif myRoll == "Y":
            return 2
        elif myRoll == "Z":
            return 3

def returnpt2(theirRoll, myRoll):
    if theirRoll == "A": # rock
        if myRoll == "X": # lose
            return 0+3 #scissors
        elif myRoll == "Y": # draw
            return 3+1 # rock
        elif myRoll == "Z": # win
            return 6+2 # paper
    elif theirRoll == "B": # paper
        if myRoll == "X":
            return 0+1 # rock
        elif myRoll == "Y":
            return 3+2 # paper
        elif myRoll == "Z":
            return 6+3 # scissors
    elif theirRoll == "C": # scissors
        if myRoll == "X":
            return 0+2 # paper
        elif myRoll == "Y":
            return 3+3 #scissors
        elif myRoll == "Z":
            return 6+1 #rock


with open('input.txt','r') as body:
    totalScore_1 = 0
    totalScore_2 = 0
    doc = body.readlines()
    for line in doc:
        a = line.split(" ")
        totalScore_1 += returnWinnersScore(a[0],a[1].strip())
        totalScore_1 += returnMyRollScore(a[1].strip())
        totalScore_2 += returnpt2(a[0],a[1].strip())

    print(totalScore_1)
    print(totalScore_2)

