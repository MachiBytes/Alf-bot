import discord
from discord.ui import Button, View
from discord.ext import commands
from src import settings
from src.verification.verify_modal import VerifyModal
from src.classes import views


async def interactive_verification_message(bot: commands.Bot):
    channel = bot.get_channel(settings.VERIFY_CHANNEL_TOKEN)

    # Clear the channel
    async for message in channel.history(limit=None):
        await message.delete()

    # Define callback
    view = views.VerifyView(bot)

    # Send the view
    await channel.send("Click the button down below to get verified!", view=view)