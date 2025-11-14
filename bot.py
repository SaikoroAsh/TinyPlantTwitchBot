import sys
from twitchio.ext import commands
from config import Config
from commands import load_all_commands
from data.save_state import save_state

class TinyPlantBot(commands.Bot):
    
    def __init__(self):
        try:
            Config.validate()
        except ValueError as e:
            print(f"\n{e}")
            sys.exit(1)
        
        super().__init__(
            token=Config.TWITCH_TOKEN,
            prefix=Config.COMMAND_PREFIX,
            initial_channels=Config.INITIAL_CHANNELS
        )
        
        print("🤖 Bot initialisé, chargement des commandes...")
        
        load_all_commands(self)
    
    async def event_ready(self):
        print(f'\n✅ Bot connecté en tant que | {self.nick}')
        print(f'📺 Channels rejoints: {", ".join([c.name for c in self.connected_channels])}')
        print('🚀 Le bot est maintenant actif!\n')
    
    async def event_message(self, message):

        if message.echo:
            return
        
        print(f'[{message.channel.name}] {message.author.name}: {message.content}')
        
        await self.handle_commands(message)
    
    async def event_error(self, error, data=None):
        print(f'❌ Erreur: {error}')


def main():
    """
    Fonction principale pour démarrer le bot
    """
    print("=" * 50)
    print("🌱 TinyPlant Twitch Bot")
    print("=" * 50)

    save_state()
    
    bot = TinyPlantBot()
    
    try:
        bot.run()
    except KeyboardInterrupt:
        print("\n\n👋 Arrêt du bot demandé...")
    except Exception as e:
        print(f"\n❌ Erreur fatale: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
