import os

with open("log.txt", "r") as rfile:
    txt = wfile.readline()
    if txt != 1:
        os.system("ifconfig en0 | grep ether > defaults.txt")

    if rfile.closed == False:
        wfile.close()

system.os("openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//'")