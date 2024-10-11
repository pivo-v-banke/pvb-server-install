docker compose exec  pvb-ovpn-master

iptables -t nat -A POSTROUTING -o tun0 -j SNAT --to-source <NEW_IP>