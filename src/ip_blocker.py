import subprocess

def block_ip(ip, dry_run=True):
    """
    Bloque une IP sur le système.
    
    Arguments :
    - ip : adresse IP à bloquer
    - dry_run : si True, n’exécute pas la commande mais l’affiche seulement
    """
    command = f"iptables -A INPUT -s {ip} -j DROP"
    
    if dry_run:
        print(f"[Dry Run] Commande pour bloquer {ip} : {command}")
    else:
        try:
            subprocess.run(command.split(), check=True)
            print(f"[Bloqué] {ip}")
        except subprocess.CalledProcessError as e:
            print(f"[Erreur] Impossible de bloquer {ip} : {e}")

def block_multiple_ips(ips, dry_run=True):
    """
    Bloque plusieurs IP.
    
    Arguments :
    - ips : liste ou dictionnaire d’IP (ex: Counter)
    - dry_run : mode test
    """
    if isinstance(ips, dict):
        ips = ips.keys()
    
    for ip in ips:
        block_ip(ip, dry_run=dry_run)

if __name__ == "__main__":
    # Exemple de test
    test_ips = ["192.168.1.15", "10.0.0.44"]
    block_multiple_ips(test_ips)
