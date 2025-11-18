"""
Commande: !water
Arrose la plante
"""
from twitchio.ext import commands
import time

is_timer_active = False

def cooldown_timer(seconds):
    
    while seconds > 0:
        global is_timer_active
        is_timer_active = True
        print(f'Cooldown: {seconds} secondes restantes')
        time.sleep(1)
        seconds -= 1
    is_timer_active = False
    print('Le cooldown est terminé.')

@commands.command(name='water')
async def water_command(ctx: commands.Context):

    if is_timer_active == True:
        await ctx.send(f'⏳ L\'arrosage est en cours, veuillez patienter @{ctx.author.name}.')
        return
    else:
        await ctx.send(f'💧 La plante a été arrosée par @{ctx.author.name}!')
        time.sleep(10)
        is_timer_active = False
        return


def setup(bot):
    bot.add_command(water_command)
