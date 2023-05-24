from .mhelp import Mhelp


async def setup(bot):
    await bot.add_cog(Mhelp(bot))
