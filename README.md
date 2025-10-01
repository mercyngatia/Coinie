Great work, Mercy 🎉 You’ve structured your assignment well — you now have:

* ✅ `bit_bot.py` (user system + CryptoBot API logic)
* ✅ `conie_buddy.py` (main entry point for chatbot)
* ✅ `users.json` (user data store with bcrypt hashed passwords)

### 2. **README.md**

````markdown
# Coinie Chatbot 

## Overview
Coinie Chatbot is a simple AI-powered crypto advisor built with Python.  
It allows users to **register/login securely** and fetch **live cryptocurrency data** from the CoinGecko API.  
The chatbot provides **basic rule-based investment advice** based on price trends and market capitalization.

---

## Features
- Secure user registration & login (bcrypt password hashing)  
- Live crypto data from [CoinGecko API](https://www.coingecko.com/en/api)  
- Rule-based investment advice:
  - Strong buy signals when prices rise > 5% with high market cap  
  - Caution on dips < -5%  
  - Neutral advice when stable  

---

## How to Run
1. Clone this repository  
   ```bash
   git clone https://github.com/mercyngatia/Coinie.git
   cd Coinie-Chatbot
````

2. Install dependencies

   ```bash
   pip install requests bcrypt
   ```
3. Run the chatbot

   ```bash
   python conie_buddy.py
   ```

---

## Screenshots

📸 Login & Register and Investment Advice
[Advice Output](Conie.png)

---

## Demo Video

[Screen recording demo link](https://www.loom.com/share/3bd272e0a6e049dc91ff201068e18bbb?sid=cd4e12df-c959-441e-ae42-14f5b83c8c0d)

---


Summary

This chatbot mimics basic AI decision-making by applying **rule-based logic** to real-time cryptocurrency data. It evaluates market trends, price changes, and capitalization, then generates personalized investment advice. Like AI, it processes inputs, applies conditions, and produces intelligent outputs that simulate human-like reasoning for financial decision support.
