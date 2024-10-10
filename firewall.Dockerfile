FROM alpine:latest AS base

WORKDIR /pivo
COPY fw_scripts/* .

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories && \
    apk add --update iptables bash

