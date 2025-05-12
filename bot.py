from telegram import Bot, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7930690523:AAE0ZKim78GEpOKy8FsQyiu9sw6xZni-rig'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Открыть Дневник", web_app={"url": "https://www.google.com"})]
    ])
    await update.message.reply_text("Нажмите кнопку 👇", reply_markup=keyboard)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()