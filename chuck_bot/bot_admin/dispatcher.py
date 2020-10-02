from chuck_bot.settings import BOT_TOKEN

from telegram import Bot
from telegram.ext import Dispatcher
from . import handlers


def setup():
    # Create bot, update queue and dispatcher instances
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot, None, workers=0, use_context=True)
    # Register handlers here
    for _, command_handlers in handlers.command_handlers.items():
        dispatcher.add_handler(command_handlers)
    for _, message_handler in handlers.message_handlers.items():
        dispatcher.add_handler(message_handler)
    return dispatcher

