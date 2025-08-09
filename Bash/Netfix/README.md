# Bash Script: netfix.sh – Network Auto-Troubleshooter
Many Linux users face “Why is my internet not working?” moments.
Instead of manually running a bunch of commands, this script can diagnose and auto-fix common network issues in one go.

Key Features
Checks if network interface is up.

Pings local gateway to confirm LAN connection.

Pings Google DNS (8.8.8.8) to confirm internet access.

Checks DNS resolution by pinging a domain (e.g., google.com).

Suggests or applies fixes:

Restart NetworkManager service.

Flush and renew DHCP.

Reset DNS cache.

# Generates a short troubleshooting report.
---

# Usage
```bash
chmod +x netfix.sh
./netfix.sh
```
💡 Why this is powerful:

Automates common troubleshooting steps that even experienced users do manually.

Saves time when network fails after suspend, VPN use, router reset, or Wi-Fi drop.

Works on most major Linux distros (NetworkManager-based).

---

Created by: Praneeth Varma Kopperla
Contact me for any collaboration:
Github - pvk-96
Email: praneethvarmakopperla@gmail.com
