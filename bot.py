from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "YOUR_BOT_TOKEN_HERE"  # replace with your token

# Sample Free Fire UID Data Generator
def generate_ff_data(count: int):
    bundles = ['Hip Hop', 'Cobra', 'Sakura', 'DJ Alok', 'Criminal']
    data_list = []
    for _ in range(count):
        uid = random.randint(1000000000, 9999999999)
        level = random.randint(30, 80)
        bundle = random.choice(bundles)
        email = f"user{uid}@gmail.com"
        password = f"{uid}@ff"
        data = f"📛 UID: {uid}\n📶 Level: {level}\n🎒 Bundle: {bundle}\n📧 Email: {email}\n🔐 Password: {password}"
        data_list.append(data)
    return "\n\n".join(data_list)

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👻 Welcome to Ghost Web FF Data Bot\n\nUse /gen10, /gen20, /gen50 or /gen100 to generate data.\nUse /support for help."
    )

# Command: /support
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛠 Support: @GhostzDK")

# Command: /gen10, /gen20, /gen50, /gen100
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    count = int(update.message.text.replace("/gen", ""))
    result = generate_ff_data(count)
    await update.message.reply_text(result)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("support", support))
app.add_handler(CommandHandler("gen10", generate))
app.add_handler(CommandHandler("gen20", generate))
app.add_handler(CommandHandler("gen50", generate))
app.add_handler(CommandHandler("gen100", generate))

if __name__ == "__main__":
    app.run_polling()
