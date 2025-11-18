"""
Commande: !light
Allume ou éteint la lumière des LEDs
"""
from twitchio.ext import commands


@commands.command(name='light')
async def light_command(ctx: commands.Context):

    await ctx.send(f'💡 La lumière des LEDs a été allumée/éteinte par @{ctx.author.name}!')


def setup(bot):
    bot.add_command(light_command)
