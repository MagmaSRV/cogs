from .launcher import launcher


def setup(bot):
    bot.add_cog(launcher(bot))
