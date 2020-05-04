from bot.bot import Clubiabot
from bot.credentials import API_KEY
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler

from bot.logger import logger

global bot
bot = Clubiabot(API_KEY)


def error_callback(update, context):
    logger.warning('Update "%s" ha provocado el error "%s"', update, context.error)


if __name__ == '__main__':
    logger.info('El bot ha iniciado')
    updater = Updater(token=API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=bot.handle_message))
    updater.start_polling()
    updater.idle()
