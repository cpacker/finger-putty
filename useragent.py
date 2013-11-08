import os

# default browser version
ppversion = "30.0.1599.69"

def getVersion():
    os.system("mdls -name kMDItemVersion /Applications/Google\ Chrome.app > version.txt")

    with open("version.txt", "r") as rfile:
        vtext = rfile.readline()
        # If the version lookup failed, replace with arbitrary version number
        if "kMDItemVersion" in vtext:
            version = vtext.split('=')[1]
            # Parse version text to only include number
            pversion = version.replace(" ","")
            ppversion = pversion.replace("\"","")
        elif "could not find" in vtext:
            ppversion = "30.0.1599.69"

        if rfile.closed == False:
            rfile.close()

def launchBrowser():
    os.system("open /Applications/Google\ Chrome.app   --args -user-agent=\"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chrome/" + ppversion + "\"")