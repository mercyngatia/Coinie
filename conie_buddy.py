# Import classes and libraries
from bit_bot import UserManager, CryptoBotAPI   #Import your custom classes from bit_bot.py
import json # For formatting and printing JSON data

# Create an instance of the user manager
manager = UserManager()
print("Welcome to Bit Bot Buddy System") 

#Ask user to register or login
choice = input("Type 'register' or 'login': ").strip().lower()

if choice == "register":
    manager.register()
    success, username = manager.login()
elif choice == "login":
    success, username = manager.login()
else:
    print("Invalid choice.")
    success = False
    
if success:
    bot = CryptoBotAPI(username)    # Create bot instance
    bot.greet_user()    # Show welcome message
    
    recommendations = bot.get_crypto_advice()   #Get investment advice
    for line in recommendations:
        print(line)     #Print each advice message





