import logging
import random
import string
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7773135647:AAHatUWgheGaBRDWKovpzEqR23bEBbzZAqE'

# Enable logging
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        "👋 Welcome to the GHOST WEB Free Fire Data Generator!\n\n"
        "⚙ Use /generate <10|20|30|40|50|100> to get Free Fire data.\n"
        "❓ Need help? Use /support"
    )

# Support command
@dp.message_handler(commands=['support'])
async def support(message: types.Message):
    await message.reply("👨‍💻 Contact @GhostzDK for support.")

# Generator logic
def generate_ff_data(amount):
    entries = []
    for _ in range(amount):
        uid = ''.join(random.choices(string.digits, k=9))
        level = random.randint(45, 80)
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@gmail.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        bundle = random.choice(["Hip Hop", "Sakura", "Criminal", "Cobra", "Galaxy Dino", "None"])

        entry = f"""🔰 𝗚𝗛𝗢𝗦𝗧 𝗪𝗘𝗕 🔰
👤 UID: `{uid}`
📶 LEVEL: `{level}`
📩 EMAIL: `{email}`
🔑 PASSWORD: `{password}`
🎒 BUNDLE: `{bundle}`
━━━━━━━━━━━━━━━
🌀 JALDI JALDI ID CHECK KARO
👑 OWNER - @GhostzDK
━━━━━━━━━━━━━━━"""
        entries.append(entry)
    return "\n\n".join(entries)

# Split large message
def split_message(text, chunk_size=4000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Generate command
@dp.message_handler(commands=['generate'])
async def generate(message: types.Message):
    try:
        count = int(message.get_args())
        if count not in [10, 20, 30, 40, 50, 100]:
            await message.reply("❌ Use only: 10, 20, 30, 40, 50, or 100")
            return
        await message.reply("⚙ Generating data, please wait...")
        data = generate_ff_data(count)
        for chunk in split_message(data):
            await message.answer(chunk, parse_mode="Markdown")
    except Exception as e:
        await message.reply(f"❌ Error occurred: {e}")

# Run the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

