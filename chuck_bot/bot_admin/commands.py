import requests

from telegram import Update
from telegram.ext import CallbackContext

from bot_admin.models import Greeting, Helper


def caps(update: Update, context: CallbackContext):
    text_caps = update['message']['text'].upper()
    context.bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def start_command(update: Update, context: CallbackContext):
    latest_greeting = Greeting.objects.latest('id')
    text = latest_greeting.hello_world
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def help_command(update: Update, context: CallbackContext):
    latest_helper = Helper.objects.latest('id')
    text = latest_helper.help
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def chuck_command(update: Update, context: CallbackContext):
    text = get_chuck_joke()
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def get_chuck_joke():
    try:
        contents = requests.get('https://api.chucknorris.io/jokes/random').json()
        joke = contents['value']
    except requests.RequestException:
        joke = "Chuck broke Internet, so we can't find new stories about him"
    return joke
