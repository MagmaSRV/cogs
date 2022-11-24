from .form import form


def setup(bot):
    bot.add_cog(form(bot))
