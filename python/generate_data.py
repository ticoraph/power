import json
from datetime import datetime

# Exemple de données générées
data = {
    "message": f"Bonjour depuis Python ! Dernière génération : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
}

# Sauvegarde dans le dossier data
with open("../data/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ data.json généré avec succès !")