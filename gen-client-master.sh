docker compose exec pvb-ovpn-master easyrsa build-client-full $1 nopass
docker compose exec pvb-ovpn-master ovpn_getclient $1 > clients/$1.ovpn
python3 patch_client.py clients/$1.ovpn