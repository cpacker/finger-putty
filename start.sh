#!/bin/bash
echo Starting...

echo 1 > log.txt

python setctl.py
echo Setting MAC address...
python macaddress.py
echo Launching Chrome with new user agent...
python useragent.py