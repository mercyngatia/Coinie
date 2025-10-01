# Import libraries
import requests # For making HTTP requests to the CoinGecko API
import json # For formatting and printing JSON data
import bcrypt  # Import for password hashing 


# Define a simple user registration and login system
class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()    # Dictionary to store usernames and password
        
    def load_users(self):
        """"Load users from JSON file"""
        try:
            with open("users.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
            
    def hash_password(self, password):
         """Hash a password for storing"""
         #Using bcrypt library directory
         salt = bcrypt.gensalt()
         hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
         return hashed_bytes.decode('utf-8')    # Convert bytes to string for JSON storage

    def verify_password(self, password, stored_hash):
        """Hash a password for storing"""
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_bytes.decode('utf-8')

    #Using passlib library
    #return bcrypt.hash(password)  
                
    def register(self):
        """Register a new user with a hashed password."""
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty")
            return
        
        if username in self.users:
            print("That username is already reqistered. Please choose a different one")
            return  #Exit early
        
        password = input("Enter password: ")
        #Hash the password before storing
        hashed_password = self.hash_password(password)
        
        self.users[username] = hashed_password
        with open("users.json", "w") as f:
            json.dump(self.users, f, indent=4)    #Save to file
        print("Registration successful")
                
    def login(self):
        """Login a user by verifying the password hash."""
        username = input("Enter username: ").strip()
        password = input("Enter password: ")
        
        if username in self.users:
            stored_hash = self.users[username]
            if self.verify_password(password, stored_hash):
                print("Login successful")
                return True, username
        
            print("Invalid credentials!")
            return False, None 
        
        print("User not found!")
        return False, None 
        

# Define the chatbot class that fetches and analyzes crypto data
class CryptoBotAPI:
    def __init__(self, user):
        self.user = user    # Store the logging-in users names
        self.base_url = "https://api.coingecko.com/api/v3"  # Base URL for CoinGecko API

    
    # Welcome Message
    def greet_user(self):
        print(f"\nHi {self.user}, I'm your CryptoBot!")
        print("Let's check out the crypto market and find smart investment options.")
        print("Crypto is risky, always do your own research.\n")
    
    
    def get_live_crypto_data(self, coins=["bitcoin", "ethereum", "Cardano"], currency="usd"):
        endpoint = f"{self.base_url}/coins/markets"     # API endpoint for market data
        params = {
            "ids": ",".join(coins),     # Join coin names into a comma-separated string
            "vs_currency": currency,    # Currency to compare against e.g USD
            "orders": "market_cap_desc",    # Sort by market cap
            "price_change_percentage": "24h,7d" # Include 24h and 7d price change
            
        }
        try:
            response = requests.get(endpoint, params=params)    # Make the API request
            response.raise_for_status() # Raise error for bad response
            return response.json()  #Return parsed JSON data   
        except Exception as e:
            return {"errors": str(e)}   #Return error message if request fails
        
# Analyze market data and give rule-based investment advice
    def get_crypto_advice(self, coins=["bitcoin", "ethereum", "cardano"], currency="usd"):
        market_data = self.get_live_crypto_data(coins, currency)    # Get live market data
    
        advice = [] # List to store advice messages
    
        # If API failed, show error
        if "errors" in market_data:
            advice.append("Failed to fetch live data: " + market_data["errors"])
        
        # Loop through each coins data
        for coin in market_data:
            name = coin["name"]     # Coin name e.g Bitcoin
            price = coin["current_price"]   #Current price in USD
            change_24h = coin.get("price_change_percentage_24h_in_currency", 0)     # 24h change
            market_cap = coin["market_cap"] #Market capitalization
        
            #Rule-based advice logic
            if change_24h > 5 and market_cap > 10_000_000_000:
                advice.append(f"{name} is booming with a {change_24h:.2f}% gain in the last 24h. Price: ${price}")
            elif change_24h < -5:
                advice.append(f"{name} is dipping ({change_24h:.2}%). Might be risky right now.")
            else:
                advice.append(f"{name} is stable. Price: ${price}. Watch for future movement.")
    
        return advice   #Return all advice messages
                
        

            
            

                
        