import random
easy_words = ["bat","ball","copy","chair","hand","shoes"]
medium_words = ["basket","laptop","mouse","manali","travel","tubelight"]
hard_words = ["synonyms","apparently","medicines","bachelors","university","neighbors"]

print("WELCOME TO THE WORD GUESSING GAME \n")
level = input("Choose the difficulty level - Easy, Medium, Hard :").lower()
if level == "easy":
    word = random.choice(easy_words)
elif level == "medium":
    word = random.choice(medium_words)
elif level == "hard":
    word = random.choice(hard_words)
else:
    print("Invalid Choice, Defaulting to easy level")
    word = random.choice(easy_words)

attempts = 0
while True:
    guess = input("Guess the word :").lower()
    attempts += 1
    
    if guess == word:
        print("CONGRATULATIONS!!🎉🎉")
        print(f"You guessed the word in {attempts} attemps.")
        break
    
    hint = " "
    for i in range (len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
            
        else:
            hint += "_"
            
    print("Hint: ", hint)
    
print("Game Over")
        
    

    