import datetime
import os

import requests
import logging
import ipaddress

logger = logging.getLogger(__name__)

DISCORD_MAIN = "https://raw.githubusercontent.com/GhostRooter0953/discord-voice-ips/refs/heads/master/custom-solutions/KindWarlock/discord-main-ips"
DISCORD_VOICE = "https://raw.githubusercontent.com/GhostRooter0953/discord-voice-ips/refs/heads/master/discord-voice-ip-list"


def is_ipv4(string):
    try:
        ipaddress.IPv4Network(string)
        return True
    except ValueError:
        return False

def get_discord_ips():
    main_ips_resp = requests.get(DISCORD_MAIN)

    if main_ips_resp.status_code == 200:
        main_ips = main_ips_resp.text.split("\n")
        main_ips = [ip.strip() for ip in main_ips]
    else:
        main_ips = []
        logger.error(
            "Discord: Could not get main ips via %s, status: %s, resp: %s",
            DISCORD_MAIN,
            main_ips_resp.status_code,
            main_ips_resp.text,
        )
    voice_ips_resp = requests.get(DISCORD_VOICE)
    if voice_ips_resp.status_code == 200:
        voice_ips = voice_ips_resp.text.split("\n")
        voice_ips = [ip.strip() for ip in voice_ips]
    else:
        voice_ips = []
        logger.error(
            "Discord: Could not get voice ips via %s, status: %s, resp: %s",
            DISCORD_MAIN,
            voice_ips_resp.status_code,
            voice_ips_resp.text,
        )

    return main_ips + voice_ips


def get_ipinfo_ips():
    return ["34.117.59.81"]

def make_backup():
    if not os.path.exists("./shared/allowed_ips"):
        return
    ts = int(datetime.datetime.utcnow().timestamp())
    with open(f"./shared/allowed_ips_{ts}.back", "w") as back_f:
        with open("./shared/allowed_ips") as f:
            back_f.write(f.read())


def clean_ips(ips) -> list[str]:
    cleaned = []
    for ip in ips:
        if is_ipv4(ip):
          cleaned.append(ip)
    return cleaned


if __name__ == "__main__":
    make_backup()
    new_ips = get_discord_ips() + get_ipinfo_ips()
    new_ips = clean_ips(new_ips)
    if not os.path.exists("shared"):
        os.mkdir("shared")
    with open("./shared/allowed_ips", "w") as f:
        for ip in new_ips:
            f.write(ip)
            f.write("\n")
