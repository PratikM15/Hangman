from nltk.corpus import words
import random

#import nltk
#nltk.download()

print("H A N G M A N")

def start_game():
    word_list = words.words()
    word = random.choice(word_list)
    hint = "-"*len(word)
    counter = 1
    attempts = []
    while counter < 9:
        print(f"\n{hint}")
        if hint == word:
            print("You guessed the word", word + "!")
            break
        else:
            letter = input("Input a letter: ")
            if letter in word and letter not in hint:
                indexes = [i for i, ltr in enumerate(word) if letter == ltr]
                for index in indexes:
                    hint = hint[:index] + letter + hint[index + 1:]
                    
            elif len(letter) != 1:
                print("You should input a single letter")
                counter += 1
            
            elif letter in attempts:
                if counter == 8:
                    print("No such letter in the word")
                else:
                    print("You already typed this letter")
                counter += 1
                
            elif not letter.islower():
                print("It is not an ASCII lowercase letter")
                counter += 1
                
            else:
                print("No such letter in the word")
                counter += 1
        attempts.append(letter)
            
    print("You are hanged!" + "The word is " + word if counter == 9 else "You survived!")
        
while True:
    print()
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        start_game()
    elif choice == 'exit':
        break
    else:
        continue

    
    
 

