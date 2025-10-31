from datetime import datetime
import os

def generate_report(failed_ips, success_ips, report_path="reports/daily_report.txt"):
    """
    Génère un rapport quotidien des connexions SSH.
    
    Arguments :
    - failed_ips : dict {ip: nombre de tentatives échouées}
    - success_ips : dict {ip: nombre de connexions réussies}
    - report_path : chemin du fichier de rapport
    """
    
    # Création du dossier reports si non existant
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    # Ouvrir le fichier en mode écriture
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== SSH Security Monitor - Rapport Quotidien ===\n")
        f.write(f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Connexions échouées
        f.write("[Connexions échouées]\n")
        if failed_ips:
            for ip, count in failed_ips.items():
                f.write(f"{ip} → {count} fois\n")
        else:
            f.write("Aucune tentative échouée détectée.\n")
        
        f.write("\n[Connexions réussies]\n")
        if success_ips:
            for ip, count in success_ips.items():
                f.write(f"{ip} → {count} fois\n")
        else:
            f.write("Aucune connexion réussie détectée.\n")
    
    print(f"Rapport généré avec succès : {report_path}")
