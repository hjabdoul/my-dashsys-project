import platform
import psutil
import json
import requests  # Nouvelle bibliothèque pour l'envoi HTTP
import time

# Pense à remplacer par l'IP "Host-Only" réelle de ta VM SERVEUR
SERVER_IP = "Add your Server IP"
URL = f"http://{SERVER_IP}:5000/api/report"

def collect_system_metrics():
    system_info = {
        "os": platform.system(),
        "os_release": platform.release(),
        "hostname": platform.node()
    }
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    ram_usage = ram.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    return {
        "machine": system_info,
        "cpu": cpu_usage,
        "ram": ram_usage,
        "disk": disk_usage
    }

if __name__ == "__main__":
    print("🚀 Lancement de l'agent de supervision...")

    # Boucle infinie pour envoyer les données toutes les 5 secondes
    while True:
        try:
            data = collect_system_metrics()
            # Envoi du JSON via une requête HTTP POST
            response = requests.post(URL, json=data)

            if response.status_code == 200:
                print(f"✅ Métriques envoyées avec succès à {SERVER_IP}")
            else:
                print(f"⚠️ Erreur serveur (Code {response.status_code})")

        except requests.exceptions.ConnectionError:
            print("❌ Impossible de contacter le serveur. Est-il allumé ?")

        # Attendre 5 secondes avant la prochaine collecte
        time.sleep(5)
