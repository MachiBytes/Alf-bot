import discord
from discord.ext import commands
from src.classes import views
from src import settings
from src.util.load_cogs import load_cogs
import random
import logging

logger = logging.getLogger("bot")


class PersistentViewBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or("@"), intents=intents)

    async def setup_hook(self):
        self.add_view(views.VerifyView(self))
        self.add_view(views.TicketView(self))

    async def on_ready(self):
        logger.info(f"User: {self.user} (ID: {self.user.id})")
        await load_cogs(self)

    async def on_member_join(self, member):
        welcome_channel = self.get_channel(settings.WELCOME_CHANNEL_TOKEN)
        custom_messages = settings.CUSTOM_MESSAGES

        await welcome_channel.send(random.choice(custom_messages).replace("{MEMBER}", member.mention))