# 🔐 SSH Security Monitor

**SSH Security Monitor** est un outil Python qui analyse les journaux SSH pour détecter les tentatives de connexion échouées, identifier les adresses IP suspectes et générer des rapports de sécurité quotidiens.  
Projet idéal pour débuter en **cybersécurité défensive (Blue Team)** et en analyse de logs.

---

## 🎯 Objectifs

- Analyser les logs SSH depuis `data/sample_auth.log`
- Détecter les échecs de connexion et les IP suspectes
- Lister les connexions réussies
- Générer un rapport automatique (`reports/daily_report.txt`)
- *(Bonus)* Simuler ou bloquer les IP malveillantes avec `iptables`

---

## 🧰 Technologies

- **Langage** : Python 3  
- **Modules** : `re`, `os`, `subprocess`, `collections`  
- **Système** : Linux (Ubuntu, Debian, Kali…)  
- **Versionnement** : Git & GitHub  


MIT License
Copyright (c) 2025 Yasser Bouchaal






