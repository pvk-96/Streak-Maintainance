# Netfix.sh: A script used to Diagnose the cause of network issues.
# Created by pvk-96
echo -e "${YELLOW}=== NetFix: Linux Network Auto-Troubleshooter ===${NC}"

# 1. Check network interface
IFACE=$(ip route | grep '^default' | awk '{print $5}')
if [[ -z "$IFACE" ]]; then
    echo -e "${RED}[!] No active network interface found.${NC}"
    echo "Try connecting to Wi-Fi or plugging in an Ethernet cable."
    exit 1
else
    echo -e "${GREEN}[✓] Active interface: $IFACE${NC}"
fi

# 2. Check LAN connectivity
GATEWAY=$(ip route | grep '^default' | awk '{print $3}')
if ping -c 1 -W 2 "$GATEWAY" &>/dev/null; then
    echo -e "${GREEN}[✓] Connected to local network (Gateway: $GATEWAY)${NC}"
else
    echo -e "${RED}[!] Cannot reach gateway ($GATEWAY).${NC}"
    echo "Trying DHCP renew..."
    sudo dhclient -r $IFACE && sudo dhclient $IFACE
fi

# 3. Check internet access (IP-based)
if ping -c 1 -W 2 8.8.8.8 &>/dev/null; then
    echo -e "${GREEN}[✓] Internet is reachable (via IP).${NC}"
else
    echo -e "${RED}[!] No internet connection (IP ping failed).${NC}"
    echo "Restarting NetworkManager..."
    sudo systemctl restart NetworkManager
fi

# 4. Check DNS resolution
if ping -c 1 -W 2 google.com &>/dev/null; then
    echo -e "${GREEN}[✓] DNS resolution working.${NC}"
else
    echo -e "${RED}[!] DNS resolution failed.${NC}"
    echo "Fixing DNS..."
    echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf >/dev/null
fi

# 5. Final Check
echo -e "${YELLOW}=== Final Status Check ===${NC}"
if ping -c 1 -W 2 google.com &>/dev/null; then
    echo -e "${GREEN}[✓] Network is now working!${NC}"
else
    echo -e "${RED}[!] Still facing issues. Manual troubleshooting required.${NC}"
fi
