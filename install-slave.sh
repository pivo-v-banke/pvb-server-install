docker compose run --rm pvb-ovpn-slave ovpn_genconfig -u udp://10.4.0.3 -N -e "local 10.4.0.3"
docker compose run --rm pvb-ovpn-slave ovpn_initpki