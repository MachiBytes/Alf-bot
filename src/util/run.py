import discord
import random
from src import settings
from src.util.load_cogs import load_cogs
from src.verification import verify
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="@", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        await load_cogs(bot)
        await verify.interactive_verification_message(bot)

    @bot.event
    async def on_member_join(member):
        welcome_channel = bot.get_channel(settings.WELCOME_CHANNEL_TOKEN)
        custom_messages = settings.CUSTOM_MESSAGES

        await welcome_channel.send(random.choice(custom_messages).replace("{MEMBER}", member.mention))

    bot.run(settings.TOKEN, root_logger=True)
