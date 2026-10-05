import os
from flask import Flask
from threading import Thread

# Render Port Keep-Alive Web Server
app = Flask('')

@app.route('/')
def home():
    return "Bot is running live!"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# பாட் தொடங்கும் முன் Web Server-ஐ இயக்கவும்
keep_alive()

# ----------------------------------------------------
# உங்கள் பழைய Telegram Bot imports & code கீழே தொடரும்...
# ----------------------------------------------------
