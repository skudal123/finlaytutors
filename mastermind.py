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
InsultGenerator = []
PraiseGenerator = []
Difficulty = 4 #Set to 4 for default dificulty, controls number of values in the GeneratedCode variable
debug = False

def doNothing():
    return

def GenerateCode(Difficulty):
    RandomCodeList = [] #create new empty list
    while (len(RandomCodeList) != Difficulty): #itterate until length of the random list is = the difficulty
        RandomCodeList.append(random.choice(AllowedValuesList)) #add random value to list from AllowedValuesList 
    return RandomCodeList

def GetEntry():
    Tempinput = input("Please enter your guess, now: ")
    if (Tempinput == ""):
        print("try writing a guess, please")
        return(GetEntry())
    else:
        Templist = list(Tempinput)
        if (len(Templist) != Difficulty):
            print("maybe less or even more? perhaps "+str(Difficulty)+" characters")
            return(GetEntry())
        else:
            numAllowed = 0
            for value in Templist:
                if value in AllowedValuesList:
                    numAllowed = numAllowed +1
            if numAllowed != Difficulty:
                print("only "+str(AllowedValuesList)+" are allowed")
                return(GetEntry())
            else:
                return(Templist)


#####TO DO######
#finish debug on this area
    if (debug == True):
        print(Templist)
 

#####To Do######
#check the entry against the random code for win or returned result
#add user feedback
#LP add score, timer and insults

def main():
    GeneratedCode = GenerateCode(Difficulty)
    #GeneratedCode = ['7','7','1','8']
    CorrectMarking = []
    GuessMarking = []
    while (len(CorrectMarking) != Difficulty):
        CorrectMarking.append('X')
    if (debug == True):
        print("Generated Code was:" + str(GeneratedCode))


    while (GuessMarking != CorrectMarking): 
        GuessMarking = []
        ValuesUsed = []
        for i in range(Difficulty):
            GuessMarking.append('-')
            ValuesUsed.append('-')

        Userinput = GetEntry()
        
        for i in range(Difficulty):
            if(Userinput[i] == GeneratedCode[i]):
                GuessMarking[i] ="X"
                ValuesUsed[i] = "Used"
        for i in range(Difficulty):
            for j in range(Difficulty):
                if(Userinput[i] == GeneratedCode[j]):
                    if GuessMarking[i] != "X" and ValuesUsed[j] != "Used":
                        GuessMarking[i] ="O"
                        ValuesUsed[j] = "Used"
                        break

        if (debug == True):
            print(GeneratedCode)
            print(ValuesUsed)
            print("")
            print(Userinput)
            print(GuessMarking)

        GuessMarking.sort(reverse=True)
        print(GuessMarking)

    print("is correct, welldone")


main()



