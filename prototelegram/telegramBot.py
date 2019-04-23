import telegram
from telegram.ext import Updater, CommandHandler
import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../keys/dw-project.json")
# Not Included
firebase_admin.initialize_app(cred, {'databaseURL': 'https://dw-project-d22fe.firebaseio.com/'})

ref = db.reference()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class myBot(telegram.Bot):
    def __init__(self, token=None, **kwargs):
        super().__init__(token, **kwargs)
        self._updater = Updater(token, use_context=True)
        self._dispatcher = self._updater.dispatcher
        self._start_handler = CommandHandler('start', self.start)
        self._dispatcher.add_handler(self._start_handler)
        self._updater.start_polling()

    def start(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

    def handlers(self, **kwargs):
        pass

bot = myBot(token='817585135:AAH51afZV9FsURDUj-SYtiOxfPjUrcRQyN4')

