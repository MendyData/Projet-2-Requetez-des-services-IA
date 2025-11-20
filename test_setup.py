# test_setup.py

import os
from dotenv import load_dotenv

print("\n" + "="*80)
print("TEST DE CONFIGURATION - POETRY + DOTENV")
print("="*80)

# Charger les variables
load_dotenv()

print(f"\nDOSSIER COURANT:    {os.getcwd()}")
print(f"FICHIER .env:       {os.path.exists('.env')}")

# Variables d'environnement
hf_token = os.getenv("API_KEY", "NON CONFIGURE")
api_url = os.getenv("API_URL", "NON CONFIGURE")
model_id = os.getenv("MODEL_ID", "NON CONFIGURE")

print(f"\nVARIABLES D'ENVIRONNEMENT:")
print(f"  HF_TOKEN:         {hf_token[:20] if len(hf_token) > 20 else hf_token}...")
print(f"  API_URL:          {api_url}")
print(f"  MODEL_ID:         {model_id}")

# Vérifier les imports
print(f"\nVERIFICATION DES IMPORTS:")
modules = {
    "requests": False,
    "PIL": False,
    "matplotlib": False,
    "numpy": False,
    "pandas": False,
    "sklearn": False,
    "torch": False,
    "transformers": False,
    "dotenv": False,
}

for module_name in modules.keys():
    try:
        __import__(module_name)
        modules[module_name] = True
        print(f"  {module_name:15} OK")
    except ImportError:
        print(f"  {module_name:15} ERREUR")

# Résumé
ok_count = sum(1 for v in modules.values() if v)
print(f"\nRESULTAT: {ok_count}/{len(modules)} modules installes")

if ok_count == len(modules):
    print("\nEtat: PRET")
else:
    print("\nEtat: ERREURS - Relancer 'poetry install'")

print("="*80 + "\n")
