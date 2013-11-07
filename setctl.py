import os

# OSX 10.8 Defaults
DEFAULT_MTU = 1500
DEFAULT_TTL = 64
DEFAULT_TCPR = 131072
DEFAULT_TCPS = 131072
DEFAULT_DFBIT = 0
DEFAULT_RFC = 1

# Set the default MTU
def setmtu(mtu_value):
    mtu = "sudo networksetup -setMTU en0 " + str(mtu_value)
    os.system(mtu)
# Set the TCP receive window size
def rwindow(window_size):
    wnd = "sudo sysctl -w net.inet.tcp.recvspace=" + str(window_size)
    os.system(wnd)
# Set the TCP send window size
def swindow(window_size):
    wnd = "sudo tcp.sendspace=" + str(window_size)
    os.system(wnd)
# Set the IP initial time-to-live
def setttl(val):
    cmd = "sudo sysctl -w net.inet.ip.ttl=" + str(val)
    os.system(cmd)
# Set kernal behavior for IPv4 header (0-2)
def dfbit(val):
    cmd = "sudo sysctl -w net.inet.ipsec.dfbit=" + str(val)
    os.system(cmd)
# Set TCP timestamp behavior (0 to disable, 1 to enable)
def stamp(val):
    cmd = "sudo sysctl -w sysctl -w net.inet.tcp.rfc1323=" + str(val)
    os.system(cmd)

# Run defaults
def defaults():
    try:
        setmtu(DEFAULT_MTU)
        rwindow(DEFAULT_TCPR)
        swindow(DEFAULT_TCPS)
        setttl(DEFAULT_TTL)
        dfbit(DEFAULT_DFBIT)
        stamp(DEFAULT_RFC)
    except Exception, e:
        print "Error setting sysctl"

def control(x):
    # Ubuntu
    if os == "Ubuntu":
        mtu = 1500
        ttl = 64
        tcpr = 131072
        tcps = 131072
        dfbit = 1
        stamp = 0
    # else if os == 2:
    #     mtu = 1500
    #     ttl = 64
    #     tcpr = 131072
    #     tcps = 131072
    #     dfbit = 1
    #     stamp = 0
    # else if os == 3:
    #     mtu = 1500
    #     ttl = 64
    #     tcpr = 131072
    #     tcps = 131072
    #     dfbit = 1
    #     stamp = 0
    try:
        setmtu(mtu)
        rwindow(tcpr)
        swindow(tcps)
        setttl(ttl)
        dfbit(dfbit)
        stamp(stamp)
    except Exception, e:
        print "Error setting sysctl"