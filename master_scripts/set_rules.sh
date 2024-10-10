iptables -F
iptables -X

# Allow traffic on the loopback interface
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow established and related connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Drop all outgoing traffic by default
iptables -P OUTPUT DROP

# Allow traffic through the VPN tunnel (tun0 interface)
iptables -A OUTPUT -o tun0 -j ACCEPT