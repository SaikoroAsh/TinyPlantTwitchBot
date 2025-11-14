# 🌱 TinyPlantTwitchBot

Bot Twitch simple, sécurisé et bien structuré pour le projet "Tiny Plant".

## 📋 Prérequis

- Python 3.8 ou supérieur
- Un compte Twitch pour le bot
- Un token OAuth Twitch
- Un Client ID Twitch

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone <votre-repo>
cd TinyPlantTwitchBot
```

### 2. Créer un environnement virtuel (recommandé)
```powershell
# Créer l'environnement virtuel
python -m venv venv

# L'activer
.\venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configuration

#### A. Obtenir un Token OAuth
1. Allez sur [Twitch Token Generator](https://twitchtokengenerator.com/)
2. Sélectionnez "Bot Chat Token"
3. Cochez les scopes: `chat:read` et `chat:edit`
4. Connectez-vous avec le compte du bot
5. Copiez le token généré (commence par `oauth:`)

#### B. Obtenir un Client ID
1. Allez sur [Twitch Developers Console](https://dev.twitch.tv/console/apps)
2. Cliquez sur "Register Your Application"
3. Remplissez les informations:
   - **Name**: TinyPlantBot (ou un autre nom)
   - **OAuth Redirect URLs**: `http://localhost` (pour un bot simple)
   - **Category**: Chat Bot
4. Copiez le Client ID généré

#### C. Configurer le fichier .env
```bash
# Copier le fichier exemple
copy .env.example .env
```

Éditez le fichier `.env` et remplissez:
```env
TWITCH_TOKEN=oauth:votre_token_ici
BOT_NICK=nom_du_bot
CLIENT_ID=votre_client_id
INITIAL_CHANNELS=votre_channel
```

## ▶️ Lancer le Bot

```bash
python bot.py
```

Si tout est configuré correctement, vous verrez:
```
==================================================
🌱 TinyPlant Twitch Bot
==================================================
✅ Configuration validée avec succès!
📝 Bot: votre_bot
📺 Channels: votre_channel
🤖 Bot initialisé, connexion en cours...

✅ Bot connecté en tant que | votre_bot
📺 Channels rejoints: votre_channel
🚀 Le bot est maintenant actif!
```

## 🎮 Commandes Disponibles

| Commande | Description | Exemple |
|----------|-------------|---------|
| `!hello` | Salue l'utilisateur | `!hello` |
| `!ping` | Vérifie que le bot répond | `!ping` |
| `!commands` | Liste toutes les commandes | `!commands` |
| `!info` | Informations sur le bot | `!info` |
| `!say <message>` | Fait répéter un message | `!say Bonjour!` |
| `!dice [faces]` | Lance un dé | `!dice 20` |
| `!8ball <question>` | Boule magique | `!8ball Vais-je gagner?` |
| `!coinflip` | Pile ou face | `!coinflip` |
| `!clear` | Nettoie le chat (mod) | `!clear` |
| `!shoutout <user>` | Shoutout un streamer (mod) | `!so @User` |

## 🔧 Structure du Projet

```
TinyPlantTwitchBot/
├── .env                    # Configuration (NE PAS COMMIT!)
├── .env.example            # Exemple de configuration
├── .gitignore              # Fichiers à ignorer
├── requirements.txt        # Dépendances Python
├── config.py               # Configuration centralisée
├── bot.py                  # Code principal du bot
├── README.md               # Documentation
├── GUIDE_COMMANDES.md      # Guide pour créer des commandes
└── commands/               # Dossier des commandes (1 fichier = 1 commande)
    ├── __init__.py         # Chargement automatique
    ├── hello.py            # Commande !hello
    ├── ping.py             # Commande !ping
    ├── dice.py             # Commande !dice
    ├── 8ball.py            # Commande !8ball
    ├── coinflip.py         # Commande !coinflip
    ├── say.py              # Commande !say
    ├── info.py             # Commande !info
    ├── commands.py         # Commande !commands
    ├── clear.py            # Commande !clear (mod)
    └── shoutout.py         # Commande !shoutout (mod)
```

## 📝 Ajouter une Nouvelle Commande

**Architecture modulaire : 1 fichier = 1 commande !**

### Étape 1 : Créer un fichier
Créez un nouveau fichier dans `commands/`, par exemple `commands/bonjour.py`

### Étape 2 : Utiliser le template
```python
"""
Commande: !bonjour
Description de votre commande
"""
from twitchio.ext import commands


@commands.command(name='bonjour')
async def bonjour_command(ctx: commands.Context):
    """
    Usage: !bonjour
    """
    await ctx.send(f'Salut @{ctx.author.name}!')


def setup(bot):
    """
    Fonction OBLIGATOIRE pour enregistrer la commande
    """
    bot.add_command(bonjour_command)
```

### Étape 3 : Redémarrer le bot
Le bot charge **automatiquement** toutes les commandes du dossier `commands/` !

### 📚 Plus d'exemples
Consultez le fichier **[GUIDE_COMMANDES.md](GUIDE_COMMANDES.md)** pour des exemples détaillés :
- Commandes avec arguments
- Commandes avec alias
- Commandes réservées aux mods
- Commandes avec état/variables
- Et bien plus !

---

## 🎨 Gestion des Commandes

### ✅ Activer une commande
Le fichier `.py` dans `commands/` est automatiquement chargé

### ❌ Désactiver une commande
Renommez le fichier avec une autre extension :
```powershell
rename commands\dice.py commands\dice.py.disabled
```

### 🗑️ Supprimer une commande
Supprimez le fichier :
```powershell
del commands\ma_commande.py
```
```

## 🔒 Sécurité

✅ **Bonnes pratiques appliquées:**
- Tokens stockés dans `.env` (jamais dans le code)
- `.env` dans `.gitignore` (ne sera jamais commit)
- Validation de la configuration au démarrage
- Gestion des erreurs

❌ **À NE JAMAIS FAIRE:**
- Commit le fichier `.env`
- Partager vos tokens publiquement
- Stocker les tokens directement dans le code

## 🐛 Dépannage

### Le bot ne se connecte pas
- Vérifiez que le token commence bien par `oauth:`
- Assurez-vous que le compte bot existe sur Twitch
- Vérifiez que le nom du channel est correct (en minuscules)

### Erreur "module not found"
```bash
pip install -r requirements.txt
```

### Le bot ne répond pas aux commandes
- Vérifiez que `handle_commands(message)` est appelé dans `event_message`
- Assurez-vous d'utiliser le bon préfixe (par défaut `!`)

## 📚 Ressources

- [TwitchIO Documentation](https://twitchio.dev/)
- [Twitch Developer Documentation](https://dev.twitch.tv/docs/)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)

## 📄 Licence

Ce projet est libre d'utilisation pour le projet Tiny Plant.

---

Créé avec ❤️ pour Tiny Plant 🌱
