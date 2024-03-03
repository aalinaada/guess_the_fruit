import random

def genrateRandomFruit():
    fruits_basket = ["pear", "apple", "banana", "cashew", "watermelon","orange", "grape"]
    return random.choice(fruit_basket)

player_name = input("What is your name? ")
scores = 0
lives = 10
fruits_basket = ["pear", "apple", "banana", "cashew", "watermelon","orange", "grape"]


print("Guess a fruit from the list: \n ", fruits_basket)

while(lives > 0):
    random_fruit = random.choice(fruits_basket)
    print("Enter your guess; a hint is the fruit has", len(random_fruit), "alphabets: ")
    guessed_fruit = input()

    if random_fruit == guessed_fruit:
        lives +=2
        scores = scores + 10
        print("You passed correctly")
    
    else:
        lives -= 2
        print("Sorry, that was wrong, It was", random_fruit)
        print("You have", lives, "lives remaining.")


print("Player name is: ",player_name)
print("Scores: ",scores)