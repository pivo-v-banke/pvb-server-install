iptables-save > /cheeseballs/ipt.back

iptables -F
iptables -X
iptables -P OUTPUT DROP


iptables -A OUTPUT -d 8.8.8.8 -j ACCEPT
iptables -A OUTPUT -d 10.5.0.3 -j ACCEPT

while IFS= read -r line; do
    iptables -A OUTPUT -d $line -j ACCEPT
done < "/cheeseballs/$1"

