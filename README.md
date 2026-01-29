# 🔐 SSH Security Monitor — Log Analysis & Threat Detection

<p align="left">
  <img src="https://img.shields.io/badge/Platform-Linux-fbbf24?logo=linux&logoColor=111827" />
  <img src="https://img.shields.io/badge/Language-Python-3776ab?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-ef4444?logo=open-source-initiative&logoColor=white" />
</p>

**SSH Security Monitor** is a Python-based security tool designed to analyze SSH authentication logs, detect failed login attempts, identify suspicious IP addresses, and generate comprehensive daily security reports.

Perfect for learning **defensive cybersecurity (Blue Team)** operations and log analysis techniques.

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🎯 Objectives](#-objectives)
- [🛠️ Technologies](#️-technologies)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📊 Output Examples](#-output-examples)
- [📁 Project Structure](#-project-structure)
- [🔍 How It Works](#-how-it-works)
- [🛡️ Security Best Practices](#️-security-best-practices)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## ✨ Features

- 🔍 **SSH log parsing** from `data/sample_auth.log`
- 🚨 **Failed login attempt detection** with IP tracking
- 📊 **Suspicious IP identification** based on threshold rules (>3 attempts)
- ✅ **Successful connection monitoring**
- 📝 **Automated daily security reports** in `reports/daily_report.txt`
- 🔒 **IP blocking simulation** with `iptables` (dry-run mode)
- 📈 **Statistical analysis** of authentication patterns
- 🎨 **Clean terminal output** with organized results

---

## 🎯 Objectives

This project aims to:

1. **Parse and analyze** SSH authentication logs from `data/sample_auth.log`
2. **Detect and count** failed connection attempts per IP address
3. **Identify suspicious IPs** with multiple failures (threshold: >3 attempts)
4. **List successful connections** with occurrence counts
5. **Generate automated reports** for daily security review in `reports/daily_report.txt`
6. **Simulate IP blocking** using `iptables` (test mode)
7. **Provide actionable insights** for system administrators

---

## 🛠️ Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3 | Core scripting and log parsing |
| **Modules** | `re`, `os`, `subprocess`, `collections` | Pattern matching, file operations, system integration |
| **System** | Linux (Ubuntu/Debian/Kali) | Target operating system |
| **Version Control** | Git & GitHub | Source code management |
| **Firewall** | `iptables` | IP blocking capabilities (simulated) |

---

## ⚙️ Installation

### Prerequisites

- **Linux-based OS** (Ubuntu 20.04+, Debian, Kali Linux)
- **Python 3.x** installed
- **Root/sudo access** (for reading system logs and iptables)
- **Git** for cloning the repository

### Quick Setup

```bash
# Clone the repository
git clone https://github.com/YasserBouchaal/ssh-security-monitor.git
cd ssh-security-monitor

# Verify project structure
ls -la

# Install Python (if not already installed)
sudo apt update
sudo apt install python3 python3-pip -y

# Install dependencies (optional, uses built-in modules)
pip3 install -r requirements.txt

# (Optional) Copy system SSH logs for analysis
sudo cp /var/log/auth.log data/sample_auth.log
```

---

## 🚀 Usage

### Running the Monitor

The main script is located in the `src/` directory. Run it from the project root:

```bash
# Navigate to src directory
cd src/

# Run the monitor
python3 main.py
```

### What Happens When You Run It:

1. **Reads logs** from `data/sample_auth.log`
2. **Analyzes** failed and successful authentication attempts
3. **Displays results** in the terminal
4. **Generates report** in `reports/daily_report.txt`
5. **Simulates blocking** suspicious IPs (dry-run mode)

### Command Options

The script currently runs with default settings. To customize:

```python
# Edit main.py to change:
# - Log file path: "data/sample_auth.log"
# - Threshold for suspicious IPs: count > 3
# - Dry-run mode: dry_run=True (change to False to actually block IPs)
```

---

## 📊 Output Examples

### Terminal Output

```
=== SSH Security Monitor ===

[Connexions échouées]
192.168.1.15 → 7 fois
10.0.0.44 → 1 fois

[Connexions réussies]
192.168.1.20 → 1 fois

[SIMULATION] Would block IP: 192.168.1.15 (7 attempts)
Rapport généré : reports/daily_report.txt
```

### Generated Report Format

**File:** `reports/daily_report.txt`

```
=== SSH Security Monitor - Rapport Quotidien ===
Date : 2025-10-31 04:17:02

[Connexions échouées]
192.168.1.15 → 7 fois
10.0.0.44 → 1 fois

[Connexions réussies]
192.168.1.20 → 1 fois
```

---

## 📁 Project Structure

```
ssh-security-monitor/
│
├── src/
│   ├── main.py                 # Main entry point - orchestrates analysis
│   ├── log_parser.py           # Log parsing and IP detection functions
│   ├── report_generator.py    # Report generation module
│   └── ip_blocker.py           # IP blocking simulation with iptables
│
├── data/
│   └── sample_auth.log         # Sample SSH authentication logs
│
├── reports/
│   └── daily_report.txt        # Generated security reports
│
├── requirements.txt            # Python dependencies (built-in modules)
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore rules
```

---

## 🔍 How It Works

### 1. Log Parsing (`log_parser.py`)

**Functions:**
- `read_local_log(filepath)` - Reads SSH log file line by line
- `detect_failed_ips(logs)` - Extracts IPs with failed authentication attempts
- `detect_successful_ips(logs)` - Extracts IPs with successful logins

**Detection Patterns:**
```python
# Failed authentication patterns
"Failed password for"
"Invalid user"
"Connection closed by authenticating user"

# Successful authentication
"Accepted password for"
"Accepted publickey for"
```

### 2. Main Analysis (`main.py`)

**Workflow:**
1. Load logs from `data/sample_auth.log`
2. Parse failed and successful authentication attempts
3. Display results in terminal
4. Generate daily report
5. Identify suspicious IPs (>3 failed attempts)
6. Simulate IP blocking (dry-run mode)

**Threshold Logic:**
```python
# IPs with more than 3 failed attempts are flagged
ips_to_block = {ip: count for ip, count in failed_ips.items() if count > 3}
```

### 3. Report Generation (`report_generator.py`)

**Output:**
- Creates/updates `reports/daily_report.txt`
- Includes timestamp, failed attempts, and successful connections
- Formatted for easy reading and archival

### 4. IP Blocking (`ip_blocker.py`)

**Simulation Mode:**
```python
# Dry-run mode (default) - only prints what would be blocked
block_multiple_ips(ips_to_block, dry_run=True)

# Active mode (use with caution)
block_multiple_ips(ips_to_block, dry_run=False)
```

**iptables Command Used:**
```bash
# Example: blocking an IP
sudo iptables -A INPUT -s 192.168.1.15 -j DROP
```

---

## 🛡️ Security Best Practices

### Recommendations

1. **Change default SSH port** (from 22 to custom port)
   ```bash
   sudo nano /etc/ssh/sshd_config
   # Change: Port 2222
   sudo systemctl restart sshd
   ```

2. **Disable root login**
   ```bash
   # In /etc/ssh/sshd_config
   PermitRootLogin no
   ```

3. **Use key-based authentication**
   ```bash
   # Generate SSH key pair
   ssh-keygen -t rsa -b 4096
   
   # Disable password authentication
   PasswordAuthentication no
   ```

4. **Implement fail2ban** for automatic blocking
   ```bash
   sudo apt install fail2ban
   sudo systemctl enable fail2ban
   ```

5. **Regular log monitoring**
   ```bash
   # Add to crontab for daily analysis
   0 8 * * * cd /path/to/ssh-security-monitor/src && python3 main.py
   ```

6. **Keep SSH updated**
   ```bash
   sudo apt update && sudo apt upgrade openssh-server
   ```

### SSH Hardening Checklist

- ✅ Change default port (22 → custom)
- ✅ Disable root login
- ✅ Enforce key-based authentication
- ✅ Limit authentication attempts (MaxAuthTries 3)
- ✅ Set idle timeout (ClientAliveInterval 300)
- ✅ Use strong passwords/passphrases (20+ characters)
- ✅ Enable two-factor authentication (2FA)
- ✅ Whitelist allowed users (AllowUsers)
- ✅ Monitor logs regularly
- ✅ Update software frequently

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Yasser Bouchaal


```

See the [LICENSE](LICENSE) file for complete details.

---

## 👤 Author

**Yasser Bouchaal**  
Cybersecurity Student | Blue Team Enthusiast

- 🎓 Specialization: Defensive Security & Log Analysis
- 💼 LinkedIn: [linkedin.com/in/yasser-bouchaal](https://linkedin.com/in/yasser-bouchaal)
- 🐙 GitHub: [@YasserBouchaal](https://github.com/YasserBouchaal)
- 📧 Contact: yasser.bouchaal@example.com

**Project created as part of network security and defensive cybersecurity learning.**

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🔮 Future Enhancements

Planned features for future versions:

- 🌐 **Real-time log monitoring** with file watchers
- 📊 **Web dashboard** using Flask for visualization
- 🗄️ **SQLite database** for historical data storage
- 📧 **Email alerts** for critical security events
- 📈 **Advanced statistics** and trend analysis
- 🔄 **Integration with fail2ban** for automated blocking
- 🌍 **GeoIP lookup** for IP location tracking
- 📱 **Mobile notifications** via Telegram/Discord

---

## 📚 Additional Resources

- 📘 [SSH Best Practices Guide](https://www.ssh.com/academy/ssh/best-practices)
- 📘 [Linux Log Analysis Tutorial](https://www.digitalocean.com/community/tutorials/how-to-view-and-configure-linux-logs)
- 📘 [Fail2ban Documentation](https://www.fail2ban.org/wiki/index.php/Main_Page)
- 📘 [Python Regex Guide](https://docs.python.org/3/library/re.html)
- 📘 [iptables Tutorial](https://www.netfilter.org/documentation/HOWTO/packet-filtering-HOWTO.html)

---

## 📝 Important Notes

> ⚠️ **Warning:** This tool is for educational and defensive security purposes only. Always ensure you have proper authorization before analyzing system logs or blocking IP addresses.

> 💡 **Tip:** Test the IP blocking functionality in a controlled environment before deploying to production. Use dry-run mode by default.

> 🔒 **Privacy:** Never share raw log files or IP addresses publicly without proper anonymization.

> 🎓 **Learning:** This project is designed for educational purposes to help students understand log analysis, pattern matching, and network security concepts.

---

## ⚡ Quick Start Guide

```bash
# 1. Clone and setup
git clone https://github.com/YasserBouchaal/ssh-security-monitor.git
cd ssh-security-monitor

# 2. Add your log file (or use sample)
sudo cp /var/log/auth.log data/sample_auth.log

# 3. Run the monitor
cd src/
python3 main.py

# 4. Check the report
cat ../reports/daily_report.txt
```

---

## 🎯 Project Status

**Status:** ✅ Functional & Tested  
**Version:** 1.0.0  
**Last Updated:** October 2024  
**Next Release:** v1.1.0 (planned - web dashboard integration)

---

**🎯 Goal Achieved: Functional SSH Security Monitoring System!**

---

<p align="center">
  Made with ❤️ for the cybersecurity community
</p>
