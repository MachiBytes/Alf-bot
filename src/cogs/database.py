from discord.ext import commands
from src.database import access_database


class Database(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    async def get_id(self, ctx, gmail):
        await ctx.send(access_database.get_id(gmail))


async def setup(bot):
    await bot.add_cog(Database(bot))
