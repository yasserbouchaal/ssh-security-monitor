import re
from collections import Counter

def read_local_log(filepath="data/sample_auth.log"):
    """
    Lit un fichier de log local (utile pour les tests sans accès root).
    Retourne le contenu complet du fichier sous forme de texte.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[Erreur] Le fichier {filepath} est introuvable.")
        return ""
    except Exception as e:
        print(f"[Erreur] Impossible de lire le fichier : {e}")
        return ""

def detect_failed_ips(logs):
    """
    Recherche toutes les IP qui ont échoué à se connecter (Failed password).
    Retourne un Counter {ip: nombre_de_tentatives}
    """
    failed_ips = re.findall(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)", logs)
    return Counter(failed_ips)

def detect_successful_ips(logs):
    """
    Recherche toutes les IP qui ont réussi à se connecter (Accepted password).
    Retourne un Counter {ip: nombre_de_connexions}
    """
    success_ips = re.findall(r"Accepted password for .* from (\d+\.\d+\.\d+\.\d+)", logs)
    return Counter(success_ips)

if __name__ == "__main__":
    # Test local
    logs = read_local_log()
    failed = detect_failed_ips(logs)
    success = detect_successful_ips(logs)

    print("=== Test du log_parser ===")
    print("\n[Connexions échouées]")
    for ip, count in failed.items():
        print(f"{ip} → {count} fois")

    print("\n[Connexions réussies]")
    for ip, count in success.items():
        print(f"{ip} → {count} fois")
