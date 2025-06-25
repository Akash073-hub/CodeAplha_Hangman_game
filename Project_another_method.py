def the(chosen,live,n,guessed_word): 
    user_letter = input("Enter the letter: ").lower()
    for i in range(size):
        if chosen[i] == user_letter:
            guessed_word[i] = user_letter
            print(f"guess :{guessed_word}")
    if live ==n:
        return guessed_word
    elif "_" not in guessed_word:
        print("You won!")
        return guessed_word
    else:
        return the(chosen, live, n+1,guessed_word)

import random
print("Welcome to the word hangman game!")
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
chosen = random.choice(words_list)
print(chosen)
size = len(chosen)
guessed_word = ["_"] * size
print(guessed_word)
var_1=the(chosen,6,0,guessed_word)
print(var_1)



