"""
Commande: !commands
Liste toutes les commandes disponibles
"""
from twitchio.ext import commands


@commands.command(name='commands', aliases=['help', 'aide', 'commandes'])
async def commands_command(ctx: commands.Context):
    
    bot = ctx.bot
    available_commands = sorted([cmd.name for cmd in bot.commands.values()])
    
    commands_list = ', '.join(f'!{cmd}' for cmd in available_commands)
    await ctx.send(f'📋 Commandes disponibles: {commands_list}')


def setup(bot):
    bot.add_command(commands_command)
