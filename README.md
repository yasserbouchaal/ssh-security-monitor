# SSH Security Monitor

SSH Security Monitor est un outil Python qui analyse les logs SSH d'un serveur Linux pour détecter les tentatives de connexion échouées et identifier les IP suspectes.

## Fonctionnalités
- Analyse des logs SSH (/var/log/auth.log ou journalctl -u ssh)
- Détection des tentatives échouées de connexion
- Comptage et identification des IP suspectes
- Liste des connexions réussies
- Génération d'un rapport quotidien
- (Bonus) Blocage automatique des IP malveillantes via iptables ou fail2ban


  License
MIT License © 2025 YASSER BOUCHAAL



