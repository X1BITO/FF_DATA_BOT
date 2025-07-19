import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "7773135647:AAHatUWgheGaBRDWKovpzEqR23bEBbzZAqE"  # Replace this with your actual bot token

SUPPORT_LINK = "https://t.me/GhostzDK"

def generate_ff_data():
    uid = str(random.randint(1000000000, 9999999999))
    level = random.randint(20, 85)
    email = f"user{random.randint(1000,9999)}@gmail.com"
    password = f"{random.randint(100000,999999)}"
    bundle = random.choice(["Hip Hop", "Sakura", "Cobra", "DJ Alok", "One Punch", "Criminal Red", "Wukong"])

    return f"""
👤 UID: {uid}
🎮 Level: {level}
📧 Email: {email}
🔐 Password: {password}
🎁 Bundle: {bundle}
    """

def generate_bgmi_data():
    uid = str(random.randint(5000000000, 5999999999))
    level = random.randint(25, 75)
    email = f"bgmi{random.randint(1000,9999)}@gmail.com"
    password = f"BGMI{random.randint(1111,9999)}"
    title = random.choice(["Conqueror", "Ace", "Crown", "Diamond", "Platinum"])
    outfit = random.choice(["M416 Glacier", "Pharaoh X-Suit", "RP Max", "Ghilli Suit"])

    return f"""
👤 UID: {uid}
🎮 Level: {level}
📧 Email: {email}
🔐 Password: {password}
🏆 Title: {title}
👕 Outfit: {outfit}
    """

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Generate Free Fire Data", callback_data="ff")],
        [InlineKeyboardButton("Generate BGMI Data", callback_data="bgmi")],
        [InlineKeyboardButton("Support", url=SUPPORT_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to Ghost Web Generator Bot 👻\nChoose an option:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "ff":
        await query.edit_message_text("Generating Free Fire data...")
        await query.message.reply_text(generate_ff_data())
    elif query.data == "bgmi":
        await query.edit_message_text("Generating BGMI data...")
        await query.message.reply_text(generate_bgmi_data())

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to generate FF or BGMI login data.\nFor help: @GhostzDK")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("support", help_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(telegram.ext.CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
