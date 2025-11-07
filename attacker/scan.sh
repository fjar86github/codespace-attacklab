#!/usr/bin/env bash
TARGET_HOST=${1:-127.0.0.1}
TARGET_PORT=${2:-8000}
echo "[*] Simple nmap scan against $TARGET_HOST:$TARGET_PORT"
nmap -Pn -p $TARGET_PORT $TARGET_HOST
echo
echo "[*] curl root page"
curl -s http://$TARGET_HOST:$TARGET_PORT/ | sed -n '1,20p'
