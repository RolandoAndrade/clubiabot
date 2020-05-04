import telegram

from bot.logger import logger


class Clubiabot(telegram.Bot):
    def __init__(self, token):
        super().__init__(token=token)

    def start(self, update, context):
        logger.info('He recibido un comando START')
        self.send_message(
            chat_id=update.message.chat_id,
            text="Soy un Achicayna, que entre los primeros pobladores de Canarias era el equivalente a un plebeyo."
        )

    def handle_message(self, update, context):
        logger.info('He recibido un mensaje')
        text = update.message.text