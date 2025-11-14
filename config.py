import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
    
    BOT_NICK = os.getenv('BOT_NICK')
    
    CLIENT_ID = os.getenv('CLIENT_ID')
    
    INITIAL_CHANNELS = os.getenv('INITIAL_CHANNELS', '').split(',')
    
    COMMAND_PREFIX = '!'
    
    @classmethod
    def validate(cls):

        if not cls.TWITCH_TOKEN:
            raise ValueError("❌ TWITCH_TOKEN manquant dans le fichier .env")
        
        if not cls.BOT_NICK:
            raise ValueError("❌ BOT_NICK manquant dans le fichier .env")
        
        if not cls.INITIAL_CHANNELS or cls.INITIAL_CHANNELS == ['']:
            raise ValueError("❌ INITIAL_CHANNELS manquant dans le fichier .env")
        
        print("✅ Configuration validée avec succès!")
        print(f"📝 Bot: {cls.BOT_NICK}")
        print(f"📺 Channels: {', '.join(cls.INITIAL_CHANNELS)}")
