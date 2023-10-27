from discord.ext import commands
from src import settings
from src.classes import views


class BotSetup(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def setup_verification(self, ctx):
        verification_channel = self.bot.get_channel(settings.VERIFY_CHANNEL_TOKEN)
        async for message in verification_channel.history():
            await message.delete()
        
        view = views.VerifyView(self.bot)
        await verification_channel.send("Click the button below to get verified!", view=view)


async def setup(bot):
    await bot.add_cog(BotSetup(bot))
