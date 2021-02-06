# Guessing Game

import random
name=input("Enter your name: ")
print(f"Hello, {name}, Welcome to the Guessing Game!")
listOfWords=["macbook", "ubuntu", "laptop", "redhat", "python", "scripting"]
word=random.choice(listOfWords)     #choosing a word from list
# getting 3 random characters from the selected word
indexes=random.sample(range(0, len(word)), 3)   
guessed=""      #this will store all the guessed characters
for i in indexes:
    guessed+=word[i]
chances=10
play=True

def playagain():
    ch=input("Do you want to play again? (Yes/No): ")
    if ch=='No':
        global play
        play=False
    else:
        #this will change all the global variables
        global word, indexes, guessed, chances
        word=random.choice(listOfWords)
        indexes=random.sample(range(0, len(word)), 3)
        guessed=""
        for i in indexes:
            guessed+=word[i]
        chances=10

while play:
    while chances!=0:
        won=True
        for ch in word:
            if ch in guessed:
                print(ch, end=" ")
            else:
                print('_', end=" ")
                won=False   #even if there is any unguessed character, it will set won to false
        if won:
            print("You Won!")
            print(f"Your score is {chances*10}%")
            playagain()
            break
        guess=input("\nGuess a character: ")
        guessed+=guess
        if guess not in word:
            chances-=1
            print("Wrong Guess!")
            print(f"You have {chances} left.")
            if chances==0:
                print("You loose!")
                playagain()
                break    