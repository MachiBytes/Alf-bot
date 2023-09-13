import discord
from discord.ui import Button, View
from discord.ext import commands
from src import settings
from src.verification.verify_modal import VerifyModal


async def interactive_verification_message(bot: commands.Bot):
    channel = bot.get_channel(settings.VERIFY_CHANNEL_TOKEN)

    # Clear the channel
    async for message in channel.history(limit=None):
        await message.delete()

    # Define callback
    async def button_callback(interaction):
        # Create the VerifyModal
        verify = VerifyModal(bot)
        await interaction.response.send_modal(verify)

    # Create the components of the View
    verify_button = Button(label="Get verified!", style=discord.ButtonStyle.primary, emoji="\u2705")
    verify_button.callback = button_callback
    view = View(timeout=None)
    view.add_item(verify_button)

    # Send the view
    await channel.send("Click the button down below to get verified!", view=view)