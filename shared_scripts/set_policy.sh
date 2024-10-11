file="/shared/allowed_ips"

# Read the file line by line
iptables -F
while IFS= read -r line
do
    # Add each IP to the iptables rules
    iptables -A FORWARD -i tun0 -o eth0 -d "$line" -j ACCEPT
done < "$file"

# Allow DNS traffic
iptables -A FORWARD -i tun0 -o eth0 -p tcp --dport 53 -j ACCEPT
iptables -A FORWARD -i tun0 -o eth0 -p udp --dport 53 -j ACCEPT

# Reject all other traffic
iptables -A FORWARD -i tun0 -o eth0 -j REJECT