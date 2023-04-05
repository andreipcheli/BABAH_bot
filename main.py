import os
import exceptions
import logging

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater
from logging.handlers import RotatingFileHandler
import song.main
import album.main
from wake_up_message import wake_up_message

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[RotatingFileHandler(
        'my_logger.log', maxBytes=50000000, backupCount=5)])

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def check_tokens():
    """Check the availability of secret tokens"""
    tokens = {
        'TELEGRAM_TOKEN': TELEGRAM_TOKEN
    }
    for token in tokens:
        if tokens[token] is None:
            raise exceptions.TokenError(f'{token} does not exist')


def wake_up(update, context):
    """Reaction to /start command"""
    chat = update.effective_chat

    context.bot.send_message(
        chat_id=chat.id,
        text=wake_up_message,
    )


def main():
    check_tokens()
    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('get_song', song.main.main))
    updater.dispatcher.add_handler(CommandHandler('get_album', album.main.main))

    updater.start_polling()
    updater.idle()
    



if __name__ == '__main__':
    main()
