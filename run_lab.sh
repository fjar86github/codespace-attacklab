#!/usr/bin/env bash
# run from repo root
set -e
echo "[*] init DB"
python3 target_app/db_init.py

echo "[*] start target app (Flask) in background on port 8000"
# run in background and redirect logs
nohup python3 target_app/app.py > target.log 2>&1 & echo $! > target.pid
sleep 1
echo "[*] target pid: $(cat target.pid)"
echo "[*] To view logs: tail -f target.log"
echo "[*] To stop: ./run_lab.sh stop"
# stop
if [ "$1" == "stop" ]; then
  if [ -f target.pid ]; then
    kill $(cat target.pid) && rm target.pid
    echo "stopped target"
  else
    echo "no pid file"
  fi
  exit 0
fi
