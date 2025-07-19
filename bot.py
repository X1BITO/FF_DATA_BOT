from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

TOKEN = "7773135647:AAHatUWgheGaBRDWKovpzEqR23bEBbzZAqE"  # Replace with your actual bot token

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Free Fire ID Generator Bot!\nUse /generate10, /generate20, /generate50 etc.")

# Support command
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("For support, contact @GhostzDK")

# Data Generator
def generate_data(count):
    results = []
    for _ in range(count):
        uid = str(random.randint(1000000000, 9999999999))
        level = random.randint(10, 80)
        bundle = random.choice(["HipHop", "Skull", "COBRa", "White444", "Alok", "DJ", "K Character", "Dragon AK"])
        data = f"UID: {uid}\nLevel: {level}\nBundles: {bundle}\nLogin: Facebook\nEmail: {uid}@gmail.com\nPassword: ghost123\n━━━━━━━━━━━━━━"
        results.append(data)
    return "\n".join(results)

# Generate Command
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1 or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /generate10 or /generate20 or /generate50")
        return

    count = int(context.args[0])
    if count not in [10, 20, 30, 40, 50, 100]:
        await update.message.reply_text("Only allowed: 10, 20, 30, 40, 50, 100")
        return

    await update.message.reply_text(generate_data(count))

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("generate10", lambda u, c: generate(u, c,)))
    app.add_handler(CommandHandler("generate20", lambda u, c: generate(u, c,)))
    app.add_handler(CommandHandler("generate30", lambda u, c: generate(u, c,)))
    app.add_handler(CommandHandler("generate40", lambda u, c: generate(u, c,)))
    app.add_handler(CommandHandler("generate50", lambda u, c: generate(u, c,)))
    app.add_handler(CommandHandler("generate100", lambda u, c: generate(u, c,)))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
