from src import settings


async def load_cogs(bot):
    for cog_file in settings.COGS_DIR.glob("*.py"):
        if cog_file != "__init__.py":
            await bot.load_extension(f"src.cogs.{cog_file.name[:-3]}")
