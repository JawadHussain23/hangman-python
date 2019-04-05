#importing the time module
import time
import math
import random
from os import system , name

def hangedman(turns):
    if turns == 6:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("---------")
    if turns == 5:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |    _______")
        print("    |    | o o |")
        print("    |    |  -  |")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("---------")
    if turns == 4:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |    _______")
        print("    |    | o o |")
        print("    |    |  -  |")
        print("    |       |")
        print("    |       |")
        print("    |       | ")
        print("    | ")
        print("    | ")
        print("    | ")
        print("---------")
    if turns == 3:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |    _______")
        print("    |    | o o |")
        print("    |    |  -  |")
        print("    |      /|\ ")
        print("    |     / | \ ")
        print("    |       | ")
        print("    |")
        print("    | ")
        print("    | ")
        print("---------")
    if turns == 2:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |    _______")
        print("    |    | o o |")
        print("    |    |  -  |")
        print("    |      /|\ ")
        print("    |     / | \ ")
        print("    |       | ")
        print("    |      / ")
        print("    |     /")
        print("    | ")
        print("---------")
    if turns == 1:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |    _______")
        print("    |    | o o |")
        print("    |    |  -  |")
        print("    |      /|\ ")
        print("    |     / | \ ")
        print("    |       | ")
        print("    |      / \ ")
        print("    |     /   \ ")
        print("    | ")
        print("---------")
    



def clear():
    _ = system('cls') 
with open('Hangman.txt') as fin:
    file = fin.read()
    lines  = file.splitlines()
    line_number =random.randrange(0, len(lines))
    word = (lines[line_number])
    
    
    
    
print word
name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play hangman!" 

print " "

#Get the word/2
free_guess = math.floor(len(word)/2)
print free_guess
#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 6
b = free_guess
j=1
# Create a while loop
while free_guess > 0:
    a = random.randint(1,b)
    
    for char in word:
        if j == a:
            guesses = char
            break
        j = j+1
    free_guess = free_guess-1

#check if the turns are more than zero
while turns > 0:         
    clear()
    hangedman(turns)
    # make a counter that starts with zero
    failed = 0             
    
    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
            # print then out the character
            print char,    

        else:
    
        # if not found, print a dash
            print "_",     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print "You won"  

    # exit the script
        break              
    print
    

    # ask the user go guess a character
    guess = raw_input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
         # print wrong
        print "Wrong"    
 
    # how many turns are left
        print "You have", + turns, 'more guesses' 
     
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print "You Loose" 
        time.sleep(1)  
print word
            
