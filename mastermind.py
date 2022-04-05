from optparse import Values
import random
import math

GeneratedCode = []
CurrentGuessList = []
NumberOfGuesses = 0
###### TO DO ######
#Find out how to track score
ScoreCount = 0
StartTime = 0
CurrentTime = 0
AllowedValuesList = ['1','2','3','4','5','6','7','8']
###### TO DO ######
#Import Insults and praise from file
#add interface
InsultGenerator = []
PraiseGenerator = []
Difficulty = 4 #Set to 4 for default dificulty, controls number of values in the GeneratedCode variable
debug = False

def doNothing():            #does nothing because it is not told to do anything. Is useless.
    return

def GenerateCode(Difficulty): #generates code 
    RandomCodeList = [] #create new empty list
    while (len(RandomCodeList) != Difficulty): #itterate until length of the random list is = the difficulty
        RandomCodeList.append(random.choice(AllowedValuesList)) #add random value to list from AllowedValuesList 
    return RandomCodeList

def GetEntry(): #returns users entry
    Tempinput = input("Please enter your guess, now: ") #asks user for entry
    if (Tempinput == "exit" or Tempinput == "quit" or Tempinput == "please stop"): #checks user entry for stop messages
        exit() #quits
    if (Tempinput == ""): #check if user entry is blank
        print("try writing a guess, please") #becomes annoyed
        return(GetEntry()) #recurse function
    else:
        Templist = list(Tempinput) #converts string into list
        if (len(Templist) != Difficulty): #checks length of list against difficulty
            print("maybe less or even more? perhaps "+str(Difficulty)+" characters")
            return(GetEntry()) #recurse function
        else:
            numAllowed = 0 #creates temp variable to add to
            for value in Templist: #checks values in list (input)
                if value in AllowedValuesList: #checks values against Allowed Values to catch not allowed characters
                    numAllowed = numAllowed +1 #adds 1 for each value check to a temp variable
            if numAllowed != Difficulty: #if an invaild charcter had been entered then...
                print("only "+str(AllowedValuesList)+" are allowed") #code says no to user
                return(GetEntry()) #recurse function
            else:
                return(Templist) #returns list of entries for other functions to use


#####TO DO######
#finish debug on this area
    if (debug == True):
        print(Templist)
 

#####To Do######
#add user feedback
#LP add score, timer and insults

def main():
    GeneratedCode = GenerateCode(Difficulty) #sets new function to output of generate code
    #GeneratedCode = ['7','7','1','8']
    CorrectMarking = [] #Creates empty list for storing Xs (correct guesses)
    GuessMarking = [] #Creates empty list for storing -s (incorrect guesses)
    while (len(CorrectMarking) != Difficulty):
        CorrectMarking.append('X') #Fills marking list Xs in quantity equal to the diffculty number
    if (debug == True): 
        print("Generated Code was:" + str(GeneratedCode))


    while (GuessMarking != CorrectMarking): #starts while loop and sets conditions
        GuessMarking = [] #Creates empty list for storing -s to be changed later
        ValuesUsed = [] #Creates empty list for storing values already used to avoid marking errors
        for i in range(Difficulty): #fills empty lists with dashes to prepare for marking 
            GuessMarking.append('-') #^
            ValuesUsed.append('-') #^

        Userinput = GetEntry() #defines new variable - gets user input
        
        for i in range(Difficulty): #checks all values in userinput in the range of difficulty - starts loop
            if(Userinput[i] == GeneratedCode[i]): #checks if a value in user nput is corrct (equal to the generated code)
                GuessMarking[i] ="X" #adds a X onto guess marking
                ValuesUsed[i] = "Used" #tells values used that this value has been used
        for i in range(Difficulty): #checks all values in userinput in the range of difficulty - starts loop
            for j in range(Difficulty): #starts second new loop
                if(Userinput[i] == GeneratedCode[j]): #checks is a value of user input is equal to all values of generated code (with the loop)
                    if GuessMarking[i] != "X" and ValuesUsed[j] != "Used": #checks if not correct in correct place and if value is not used already
                        GuessMarking[i] ="O" #adds a O onto guess marking
                        ValuesUsed[j] = "Used" #tells values used that this value has been used
                        break #ends current cycle of loop which is effectively ending the loop entirely

        if (debug == True):
            print(GeneratedCode)
            print(ValuesUsed)
            print("")
            print(Userinput)
            print(GuessMarking)

        GuessMarking.sort(reverse=True) #shuffles guess marking into acceptable order as not to give too much information away to player
        print(GuessMarking) #prints guess marking in new and improved order

    print("is correct, welldone") #welldone message for beatng the game


main() #is main



