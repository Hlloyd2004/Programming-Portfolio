# Imports the random number function
import random
# Saves the random number to the variable called secret_number
secret_number = random.randint(0, 10)

number = 0

print(
"""
+================================+
|        My Guessing game.       |
+================================+
| Welcome to my game.            |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
while number != secret_number:
     
     number = int(input("Please guess my number"))
     
     if number == secret_number:
        print("Well done you have guessed my number. Thank you for playing")
        
     else:
         print("WRONG!! You're stuck in my loop.")