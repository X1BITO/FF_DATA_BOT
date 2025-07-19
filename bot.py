import os
import random
import telebot
import time

BOT_TOKEN = os.getenv("BOT_TOKEN", "7773135647:AAHatUWgheGaBRDWKovpzEqR23bEBbzZAqE")
bot = telebot.TeleBot(BOT_TOKEN)

OWNER = "@GhostzDK"
BUNDLES = ["Cobra", "Joker", "Angelic", "Hip Hop", "Sakura", "Elite Pass", "Gold Dress"]

def generate_data():
    uid = str(random.randint(4000000000, 4999999999))
    level = random.randint(40, 75)
    email_number = str(random.randint(7000000000, 9999999999))
    password = "jack999"
    bundles = " + ".join(random.sample(BUNDLES, 3))
    return f"""🔥 𝔄𝔄𝔊𝔜𝔄 𝔇𝔄𝔗𝔄 🔥  
📛 𝕌𝕀𝔻: {uid}  
📶 𝕃𝕠𝕘𝕚𝕟: 𝔽𝕒𝕔𝕖𝕓𝕠𝕠𝕜  
🎮 𝕃𝕖𝕧𝕖𝕝: {level}  

🎯 𝔼𝕄𝔸𝕀𝕃 - {email_number}  
𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿 - {password}  

👕 𝔹𝕦𝕟𝕕𝕝𝕖𝕤: {bundles}  

𝔻𝔸𝕋𝔸 ℙ𝕆𝕎𝔼ℝ - 💀Ghost web💀  

🚨 𝕁𝔸𝕃𝔻𝕀 𝕁𝔸𝕃𝔻𝕀 𝕀𝔻 ℂℍ𝔼ℂ𝕂 𝕂𝔸ℝ𝕆 🚨  

👑 𝕆𝕎ℕ𝔼ℝ - {OWNER}"""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to FF Data Generator Bot 💀
Use /generate 10 or 20 or 50 to get FF data.
Use /support to contact owner.")

@bot.message_handler(commands=['support'])
def support(message):
    bot.reply_to(message, "👑 Contact Owner: @GhostzDK")

@bot.message_handler(commands=['generate'])
def generate(message):
    try:
        count = int(message.text.split()[1])
        if count > 100: count = 100
        for _ in range(count):
            bot.send_message(message.chat.id, generate_data())
            time.sleep(1)
    except:
        bot.reply_to(message, "⚠️ Use command like: /generate 10, /generate 50 etc.")

bot.polling()
