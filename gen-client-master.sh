docker compose run --rm pvb-ovpn-master easyrsa build-client-full $1 nopass
docker compose run --rm pvb-ovpn-master ovpn_getclient $1 > $1.ovpn
