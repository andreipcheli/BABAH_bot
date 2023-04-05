import os
import exceptions
import logging

from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater
from logging.handlers import RotatingFileHandler

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


def my_timetable():
    """Show the timetable for a current day of the week"""
    day_timetable = {
        'monday': '',
        'tuesday': '',
        'wednesday': '',
        'thursday': '',
        'friday': '',
        'saturday': '',
        'sunday': '',
    }


def what_to_do():
    """Show an activity for a current time"""


def say_hi(update, context):
    """Reaction to /start command"""
    chat = update.effective_chat
    name = update.message.chat.first_name

    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}, я BABAH'.format(name),
    )


def respond_with_Z_pic():
    """Respond with Z picture for the unknown message"""


def be_with_us():
    """Join ЧВК «Редан» Амстердам community"""


def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_handler(CommandHandler('start', say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
