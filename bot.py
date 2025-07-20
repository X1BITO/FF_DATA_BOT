import os
import random
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = os.getenv("BOT_TOKEN")

FF_BUNDLES = [
    "💀 UID: {uid} | Level: {level} | Bundle: {bundle}",
    "🎯 UID: {uid} | Level: {level} | Bundle: {bundle}",
    "🔥 UID: {uid} | Level: {level} | Bundle: {bundle}",
    "👻 UID: {uid} | Level: {level} | Bundle: {bundle}",
    "👑 UID: {uid} | Level: {level} | Bundle: {bundle}"
]
BUNDLES = ['Hip Hop', 'Criminal', 'Cobra', 'Alok', 'White 444', 'DJ Alok', 'Skull King']

def generate_data(n):
    data = []
    for _ in range(n):
        uid = random.randint(1000000000, 9999999999)
        level = random.randint(20, 75)
        bundle = random.choice(BUNDLES)
        line = random.choice(FF_BUNDLES).format(uid=uid, level=level, bundle=bundle)
        data.append(line)
    data.append("\n🚨 JALDI JALDI ID CHECK KARO \nOWNER - @GhostzDK")
    return "\n".join(data)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to Ghost Web 🔥\nUse /gen10, /gen20, ..., /gen100 to generate data.\nUse /support for help.")

def support(update: Update, context: CallbackContext):
    update.message.reply_text("🛠 Contact Support: @GhostzDK")

def make_gen_cmd(n):
    def cmd(update: Update, context: CallbackContext):
        update.message.reply_text("⚡ Generating Data...")
        time.sleep(1)
        update.message.reply_text(generate_data(n))
    return cmd

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("support", support))
    for num in [10, 20, 30, 40, 50, 100]:
        dp.add_handler(CommandHandler(f"gen{num}", make_gen_cmd(num)))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()