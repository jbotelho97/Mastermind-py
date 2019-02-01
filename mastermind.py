#Author: Jack Botelho
#Due: May 2nd, 2016
#This program will play a game of mastermind with the user being the guesser
#and the computer being the codemaker

import random
ALL_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
def codeGen():
    #Where the code is randomly generated.
    code = []
    code.append(random.randint(0,5))
    code.append(random.randint(0,5))
    code.append(random.randint(0,5))
    code.append(random.randint(0,5))
    return code

def userGuess():
    guess = []
    print("Enter a combinatation of colors.")
    print("0 = red")
    print('1 = orange')
    print('2 = yellow')
    print('3 = green')
    print('4 = blue')
    print('5 = purple')
    print('==========')
    #Loops through to give the user four entries into his or her code.
    for i in range(4):
        temp = int(input("Enter a guess between 0-5: "))
        guess.append(temp)
    print("Your guess is: ", ALL_COLORS[guess[0]], ALL_COLORS[guess[1]],ALL_COLORS[guess[2]],ALL_COLORS[guess[3]])
    return guess

def checkFor1(userGuess, code):
    hint = []
    #Copies the code to a new list that will have modifications done to it.
    codeTemp = []
    for i in range(len(code)):
       codeTemp.append(code[i]) 
    j = 0
    while j < len(userGuess):
        i = 0
        found = False
        while i < len(codeTemp) and found == False:
            if userGuess[j] == codeTemp[i]:
                found = True
                hint.append(1)
                codeTemp.pop(i)#If the color appears in the code somewhere
                #We remove it from the temp code holder to prevent multiples
                #of the same number appearing. Then we add a one to the hint.
            else:
                i += 1
        j += 1
    hint = checkFor2(userGuess, code, hint)#This will turn any 1's where the position
    #is correct to 2's
    return hint

def checkFor2(userGuess, code, hint):
    i = 0
    while i < len(code):
        if userGuess[i] == code[i]:
            hint.pop(0)
            hint.append(2)
            #If the positions are both correct we remove a 1 and replace it with a two
        i += 1
    return hint

def main():
    print("Welcome to Mastermind!")
    code = codeGen()
    solved = False
    guess = 10
    while solved == False and guess > 0:
        userguess = userGuess()
        hint = checkFor1(userguess, code)
        print("Your hint is: ")
        print(hint)
        if hint == [2, 2, 2, 2]: #This will be satisfied if the user copies the code exactly.
            solved = True
            guess = 0
            print("You Win!")
        else:
            guess -= 1
            print("You have", guess, "guess(es) remaining!")
            print("Try another guess!")
    print("Game Over! The correct code was: ")
    print(code)
    

        
