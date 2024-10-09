FROM ubuntu:22.04 as base
WORKDIR app
ENV DEBIAN_FRONTEND=noninteractive
ENV AUTO_INSTALL=y
COPY openvpn-install.sh .
RUN apt-get update && \
    apt-get clean && apt-get -y update && apt-get install -y locales curl && \
    apt-get install -y php apache2 curl openvpn zip unzip bridge-utils && \
    apt-get install nano \

RUN mkdir -p /dev/net && \
    mknod /dev/net/tun c 10 200 && \
    chmod 600 /dev/net/tun && \
    ./openvpn-install.sh

