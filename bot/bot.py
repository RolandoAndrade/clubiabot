from random import randint

import telegram

from bot.credentials import USER_PASSWORD
from bot.logger import logger

wrong_command_text = "Error, el comando no está siendo empleado de la manera adecuada"

wrong_password_text = "Error, la contraseña es incorrecta"

start_text_quotes = ['Vale vale, ya me inicio', 'Ejecutar orden 66, digo, iniciar el bot', 'A sus órdenes amo']

welcome_text = "Bienvenido {username},\n " \
               "con orgullo estamos muy felices de que te unas a la comunidad de Inteligencia" \
               " Artificial en Venezuela, seguro que juntos la pasaremos muy bien. " \
               "Antes de comenzar nos gustaría que nos hablaras un poco de ti " \
               "¿Qué te trae por acá?, ¿Qué experiencias tienes en el área?, " \
               "¿Crees que la IA nos destruirá?, ¿Qué expectativas tienes? y cualquier otra cosa que creas que pueda ser " \
               "interesante, ¡Seguro tienes muchas historias que contar! ¿Estás listo para iniciar?"


class Clubiabot(telegram.Bot):
    def __init__(self, token):
        super().__init__(token=token)
        self.welcome_text = welcome_text

    def start(self, update):
        logger.info('He recibido un comando START')
        try:
            self.send_message(
                chat_id=update.message.chat_id,
                text=start_text_quotes[randint(0, len(start_text_quotes))]
            )
        except:
            self.send_message(
                chat_id=update.message.chat_id,
                text="No tengo mensaje por defecto"
            )
            logger.warn('No hay mensajes predefinidos')

    def handle_message(self, update):
        logger.info('He recibido un mensaje')
        text = update.message.text

    def add_group(self, update):
        logger.info('Alguien ha entrado al grupo')
        for member in update.message.new_chat_members:
            update.message.reply_text(self.welcome_text.format(
                username=member.username))

    def update_welcome_text(self, update):
        logger.info('He recibido un comando UPDATE WELCOME TEXT')
        text = update.message.text
        try:
            text = text.split(" ", 2)
            if text[1] == USER_PASSWORD:
                logger.info("Contraseña correcta")
                self.welcome_text = text[2]
            else:
                logger.info("Contraseña incorrecta")
                update.message.reply_text(wrong_password_text)
        except:
            self.send_message(
                chat_id=update.message.chat_id,
                text=wrong_command_text
            )
            logger.info('Error en comando introducido')

    def receive_message(self, update):
        text = update.message.text
        if text is None:
            member = update.message.new_chat_members
            if len(member) > 0:
                self.add_group(update)
        else:
            if "/start" in text:
                self.start(update)
            elif "/update_welcome_text" in text:
                self.update_welcome_text(update)
            else:
                self.handle_message(update)
