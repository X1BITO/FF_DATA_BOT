import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

# ⚙️ Your bot token
TOKEN = "7773135647:AAHatUWgheGaBRDWKovpzEqR23bEBbzZAqE"

# 🧠 Random data generator
def generate_data(count: int) -> str:
    data_list = []
    for _ in range(count):
        uid = random.randint(1000000000, 9999999999)
        level = random.randint(35, 80)
        bundle = random.choice(["HipHop", "Sakura", "Cobra", "Alok", "Criminal", "None"])
        email = f"user{random.randint(1000,9999)}@gmail.com"
        password = f"{random.randint(100000,999999)}"
        entry = f"👤 UID: {uid}\n📊 Level: {level}\n🎒 Bundle: {bundle}\n📧 Email: {email}\n🔐 Password: {password}"
        data_list.append(entry)
    return "\n\n".join(data_list)

# 🎮 /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Welcome to *Ghost Web Free Fire Data Generator*!\n\n"
        "Use /gen10, /gen20, /gen50, or /gen100 to generate data.\n"
        "Need help? Use /support",
        parse_mode="Markdown"
    )

# 🛠 Support command
def support(update: Update, context: CallbackContext):
    update.message.reply_text("📞 Support: @GhostzDK")

# 📦 Data generation commands
def gen10(update: Update, context: CallbackContext):
    update.message.reply_text(generate_data(10))

def gen20(update: Update, context: CallbackContext):
    update.message.reply_text(generate_data(20))

def gen50(update: Update, context: CallbackContext):
    update.message.reply_text(generate_data(50))

def gen100(update: Update, context: CallbackContext):
    update.message.reply_text(generate_data(100))

# 🚀 Main function
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("support", support))
    dp.add_handler(CommandHandler("gen10", gen10))
    dp.add_handler(CommandHandler("gen20", gen20))
    dp.add_handler(CommandHandler("gen50", gen50))
    dp.add_handler(CommandHandler("gen100", gen100))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
