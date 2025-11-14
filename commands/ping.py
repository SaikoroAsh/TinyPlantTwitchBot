"""
Commande: !ping
Vérifie que le bot est réactif
"""
from twitchio.ext import commands


@commands.command(name='ping')
async def ping_command(ctx: commands.Context):

    await ctx.send(f'🏓 Pong @{ctx.author.name}!')


def setup(bot):
    bot.add_command(ping_command)
