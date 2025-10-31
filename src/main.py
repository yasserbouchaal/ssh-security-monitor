from log_parser import read_local_log, detect_failed_ips, detect_successful_ips
from report_generator import generate_report
from ip_blocker import block_multiple_ips

def main():
    print("=== SSH Security Monitor ===\n")

    logs = read_local_log("data/sample_auth.log")
    if not logs:
        print("Aucun log disponible.")
        return

    failed_ips = detect_failed_ips(logs)
    success_ips = detect_successful_ips(logs)

    # Affichage terminal
    print("[Connexions échouées]")
    if failed_ips:
        for ip, count in failed_ips.items():
            print(f"{ip} → {count} fois")
    else:
        print("Aucune tentative échouée détectée.")

    print("\n[Connexions réussies]")
    if success_ips:
        for ip, count in success_ips.items():
            print(f"{ip} → {count} fois")
    else:
        print("Aucune connexion réussie détectée.")

    # Génération du rapport
    generate_report(failed_ips, success_ips)

    # Sélection des IP suspectes pour blocage
    ips_to_block = {ip: count for ip, count in failed_ips.items() if count > 3}

    # Blocage des IP suspectes (mode test)
    block_multiple_ips(ips_to_block, dry_run=True)

if __name__ == "__main__":
    main()

