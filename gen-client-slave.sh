docker compose run --rm pvb-ovpn-slave easyrsa build-client-full $1 nopass
docker compose run --rm pvb-ovpn-slave ovpn_getclient test1 > $1.ovpn