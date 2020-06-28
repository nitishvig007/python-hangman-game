

import random
name=input("Enter your name : ")
print("WELCOME !",name)
print("---------------------")
print("Guess the word in 10 attempts and save the man!")
print("(Hint : The word is related to hollywood movie released in 2013)")
print("HAPPY GUESSING :)")
print("|-|-|-|-|-|-|-|-|-|-|-|")
print("Enter valid letters i.e 'abcdefghijklmnopqrstuvwxyz'")
        

def hangman():
    word=random.choice(["avengers"])
    validLetters="abcdefghijklmnopqrstuvwxyz"
    turns=10
    guessmade=''

    while len(word) > 0:
        mainWord=""
        missed=0
        #print("Enter valid letters i.e 'abcdefghijklmnopqrstuvwxyz'")
        for letter in word:
            if letter in guessmade:
                mainWord=mainWord+letter
            else:
                mainWord = mainWord+"_"+" "

        if mainWord == word:
            print(mainWord)
            print("You WIN")
            result = ""
            break
        else :
            result = word
        print("Guess the word:",mainWord)
        guess=input()

        if guess in validLetters:
            guessmade=guessmade+guess
        else:
            print('You entered incorrectly , enter using "abcdefghijklmnopqrstuvwxyz"')
            guess = input()

        if guess not in word :
            turns=turns - 1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break
    return result
            

        
           
output = hangman()
if len(output) != 0 :
    print("The correct word is : ", output)
else :
    pass

print()
