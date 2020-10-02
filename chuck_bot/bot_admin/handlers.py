from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from bot_admin import commands

command_handlers = {
    '/start': CommandHandler('start', commands.start_command),
    '/help': CommandHandler('help', commands.help_command),
    '/chuck': CommandHandler('chuck', commands.chuck_command)
}

message_handlers = {
    '/caps': MessageHandler(Filters.text, commands.caps)
}