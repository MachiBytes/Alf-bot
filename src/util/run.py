from src import settings
from src.classes import bot_class


def run():
    bot = bot_class.PersistentViewBot()
    bot.run(settings.TOKEN, root_logger=True)
