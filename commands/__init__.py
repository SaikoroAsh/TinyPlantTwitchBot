"""
Package des commandes
Charge automatiquement toutes les commandes du dossier
"""
import os
import importlib
from pathlib import Path

def load_all_commands(bot):
    commands_dir = Path(__file__).parent
    command_files = [f.stem for f in commands_dir.glob('*.py') if f.stem != '__init__']
    
    print(f"\n📦 Chargement de {len(command_files)} commande(s):")
    
    loaded = 0
    for command_name in sorted(command_files):
        try:
            # Import dynamique du module
            module = importlib.import_module(f'commands.{command_name}')
            
            # Appelle la fonction setup() du module
            if hasattr(module, 'setup'):
                module.setup(bot)
                print(f"  ✅ {command_name}.py")
                loaded += 1
            else:
                print(f"  ⚠️  {command_name}.py (pas de fonction setup())")
                
        except Exception as e:
            print(f"  ❌ {command_name}.py - Erreur: {e}")
    
    print(f"\n✅ {loaded}/{len(command_files)} commande(s) chargée(s)\n")
