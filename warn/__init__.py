from .warn import Warn


async def setup(bot):
    await bot.add_cog(Warn(bot))
