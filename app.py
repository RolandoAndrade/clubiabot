from flask import Flask, request
import telegram

from bot.bot import Clubiabot
from bot.credentials import API_KEY, URL
from bot.logger import logger

global bot
global TOKEN
TOKEN = API_KEY
bot = Clubiabot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    logger.info("Se ha recibido una petición")
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    bot.receive_message(update)
    return 'Logrado'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    logger.info("El bot está iniciando, un momento por favor...")
    app.run(threaded=True)
