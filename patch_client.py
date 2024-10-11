import os.path
import sys

import requests


def get_real_ip():
    info_resp = requests.get("https://ipinfo.io")
    ip = info_resp.json()["ip"]
    return ip


def main():
    client = sys.argv[1]
    new_lines = []
    real_ip = get_real_ip()
    with open(client, "r") as f:
        for line in f.readlines():
            if line.startswith("remote "):
                new_line = f"remote {real_ip} 1195"
            if line.startswith("redirect-gateway "):
                continue
            else:
                new_line = line
            new_lines.append(new_line)

    if os.path.exists("./shared/allowed_ips"):
        new_lines.append("route-nopull\n")
        with open("./shared/allowed_ips") as f:
            allowed_ips = f.readlines()
            for ip in allowed_ips:
                ip = ip.strip()
                new_lines.append(f"route {ip} 255.255.255.255\n")

    base_file_dir = os.path.dirname(client)
    base_filename = os.path.basename(client)

    with open(f"{base_file_dir}/ds_{base_filename}", "w") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    main()
