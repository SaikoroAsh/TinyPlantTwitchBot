"""
Commande: !status
Donne le statut actuel de la capsule Tiny Plant
"""
from twitchio.ext import commands
import json


@commands.command(name='status', aliases=['etat', 'statut'])
async def status_command(ctx: commands.Context):

    with open('data/state.json', 'r') as f:
        state = json.load(f)
    
    await ctx.send(
        f"Statut de la capsule Tiny Plant: {state['sensors']['humidity_soil']}% d'humidité au sol, {state['sensors']['temperature']}°C, lumière modérée 🌿"
    )


def setup(bot):
    bot.add_command(status_command)
