"""
Commande: !info
Explique le projet Tiny Plant
"""
from twitchio.ext import commands


@commands.command(name='info', aliases=['projet'])
async def info_command(ctx: commands.Context):

    await ctx.send(
        '🌱 TinyPlant Bot - Un bot pour le projet Tiny Plant! '
        '| Créé avec TwitchIO 🐍'
    )


def setup(bot):
    bot.add_command(info_command)
