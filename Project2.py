import random
print("Welcome to the word hangman game!")
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
chosen = random.choice(words_list)
print(chosen)
size = len(chosen)
guessed_word = ["_"] * size
print(guessed_word)
live = 6
n = 0
while n != live:
    user_letter = input("Enter the letter: ").lower()
    count=0
    for i in range(size):
        if chosen[i] == user_letter:
            guessed_word[i] = user_letter
            print(f"guess :{guessed_word}")
            count+=1
    if count == 0:
        live -= 1
    if "_" not in guessed_word:
        print("You won!")
        break
print(guessed_word)
format = "".join(guessed_word)
print(format)  


