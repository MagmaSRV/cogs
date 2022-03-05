from .report import report


def setup(bot):
    bot.add_cog(report(bot))
