"""
Commande: !info
Donne des informations sur le bot
"""
from twitchio.ext import commands


@commands.command(name='info', aliases=['about'])
async def info_command(ctx: commands.Context):
    
    await ctx.send(
        '🌱 TinyPlant Bot - Un bot pour le projet Tiny Plant! '
        '| Créé avec TwitchIO 🐍'
    )


def setup(bot):
    bot.add_command(info_command)
