"""
Commande: !hello
Salue l'utilisateur qui lance la commande
"""
from twitchio.ext import commands


@commands.command(name='hello', aliases=['salut', 'bonjour'])
async def hello_command(ctx: commands.Context):

    await ctx.send(f'🌱 Bonjour @{ctx.author.name}! Je suis TinyPlant Bot!')


def setup(bot):
    bot.add_command(hello_command)
