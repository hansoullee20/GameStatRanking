import pandas as pd
import numpy as np

from random import seed
from random import randint

from random import choice
from string import ascii_uppercase


import random


#Generate random string of n length
def generateID(n):
    id=''.join(choice(ascii_uppercase) for i in range(n))
    return id

#Generate play results in order
# 1: win, 0: loss
def generatePlay(p):
    key = ""

    for i in range(p):
        temp = str(random.randint(0, 1))
        key += temp

    return key

# Return total number of plays
def totalPlaytime(n):
    return len(n)

# Returns number of consecutive 1's in generatePlay
def consecutiveLength(s):
    consects=s.split("0")
    consects_len = [len(x) for x in consects if len(x)!= 0]
    return consects_len

# Calculate User Score
def calculateScore(ls):
    ls_tmp=[x*2 if x!=1 else x for x in ls]
    return sum(ls_tmp*5)

# Combine the above functions to generate a user statistics
# The function returns a list of UserID, player win/loss sequence, total playtime, and the score
# n: length of a randomized ID
# p: length of a randomized win/loss sequence. 0 is loss 1 is won.
def UserStats(n,p):
    ID=generateID(n)
    playSeq=generatePlay(p)
    totalPlay=totalPlaytime(playSeq)
    winsCount=consecutiveLength(playSeq)

    totalScore=calculateScore(winsCount)

    userScore=[ID, playSeq, totalPlay, totalScore]

    return userScore

columnsName=['ID', 'PlayResults', 'PlayTime', 'Score']

# Enter the number of players and maximum played hours.
# This function returns the game statistics
def generateGameStat(df, players, maxPlaytime):
    for x in range(players):
        # n: length of a randomly generated ID
        # p: length of a randomly generated win/loss stat
        n, p = randint(1,10), randint(1,maxPlaytime)
        userstat=UserStats(n, p)
        df=df.append(pd.DataFrame([userstat], columns=columnsName), ignore_index=True)
    return df


# Change the below variables for different statistics
playerNumbers=200
maxPlaytime=10001

rank=[x for x in range(1, playerNumbers+1)]

df=pd.DataFrame(columns=columnsName)
df=generateGameStat(df, playerNumbers, maxPlaytime)
df=df.sort_values(by=['Score', 'PlayTime'], ascending=[False, True], ignore_index=True)
df.insert(0, 'Rank', rank)


print(df)