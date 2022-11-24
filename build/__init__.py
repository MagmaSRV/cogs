from .build import build


def setup(bot):
    bot.add_cog(build(bot))
