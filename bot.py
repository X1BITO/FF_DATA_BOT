from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import random
import os

TOKEN = os.getenv("BOT_TOKEN") or "7773135647:AAHatUWgheGaBRDWKovpzEqR23bEBbzZAqE"

# BGMI-style Free Fire Data Generator
def generate_data(count):
    uid_start = 1000000000
    data_list = []
    for _ in range(count):
        uid = str(uid_start + random.randint(10000, 99999))
        level = random.randint(50, 85)
        bundle = random.choice(["HipHop", "Sultan", "Cobra", "Venom", "Alok"])
        email = f"user{random.randint(1000,9999)}@gmail.com"
        password = f"pass{random.randint(1000,9999)}"
        data = f"""╭─────────────⭓
├ UID: {uid}
├ Level: {level}
├ Email: {email}
├ Password: {password}
├ Bundle: {bundle}
╰─────────────⭓"""
        data_list.append(data)
    return "\n\n".join(data_list)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Generate 10", callback_data="gen_10")],
        [InlineKeyboardButton("Generate 20", callback_data="gen_20")],
        [InlineKeyboardButton("Generate 30", callback_data="gen_30")],
        [InlineKeyboardButton("Generate 40", callback_data="gen_40")],
        [InlineKeyboardButton("Generate 50", callback_data="gen_50")],
        [InlineKeyboardButton("Generate 100", callback_data="gen_100")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👑 Welcome to Free Fire Data Generator Bot 👑\n\nSelect how many entries you want to generate:", reply_markup=reply_markup)

# /support command
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Contact our team:\n@GhostzDK")

# Button handling
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    count = int(query.data.split("_")[1])
    await query.message.reply_text("⚡ Generating data...")
    result = generate_data(count)
    await query.message.reply_text(result)

# Main bot setup
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
