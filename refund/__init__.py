from .refund import refund


def setup(bot):
    bot.add_cog(refund(bot))
