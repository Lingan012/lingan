import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("வணக்கம்! Mokka Comedy Bot தயார்!")

if __name__ == '__main__':
    # Token Environment Variable மூலம் பெறப்படும்
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("Error: BOT_TOKEN கிடைக்கவில்லை!")
    else:
        app = ApplicationBuilder().token(token).build()
        app.add_handler(CommandHandler("start", start))
        print("Bot இயங்குகிறது...")
        app.run_polling()
