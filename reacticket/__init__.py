from .request import Request


async def setup(bot):
    await bot.add_cog(Request(bot))
