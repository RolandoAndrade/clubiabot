from random import randint

import telegram

from bot.logger import logger

start_text = ['Vale vale, ya me inicio', 'Ejecutar orden 66, digo, iniciar el bot', 'A sus órdenes amo']


class Clubiabot(telegram.Bot):
    def __init__(self, token):
        super().__init__(token=token)

    def start(self, update, context):
        logger.info('He recibido un comando START')
        self.send_message(
            chat_id=update.message.chat_id,
            text=start_text[randint(0,len(start_text))]
        )

    def handle_message(self, update, context):
        logger.info('He recibido un mensaje')
        text = update.message.text

    def add_group(self, update, context):
        for member in update.message.new_chat_members:
            update.message.reply_text("Bienvenido {username},\n"
                                      "con orgullo estoy feliz de que te unas a la comunidad de Inteligencia "
                                      "Artificial en Venezuela, seguro que juntos la pasaremos muy bien. "
                                      "Antes de comenzar nos gustaría que nos hablaras un poco de ti "
                                      "¿Qué te trae por acá?, ¿Qué experiencias tienes en el área?, "
                                      "¿Crees que la IA nos destruirá?, ¿Qué expectativas tienes? y cualquier otra cosa que creas que pueda ser"
                                      "interesante, ¡Seguro tienes muchas historias que contar! ¿Estás listo para iniciar?".format(
                username=member.username))
