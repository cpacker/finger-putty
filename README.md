Finger Putty
============

Finger Putty is an OS fingerprint spoofer that modifies the TCP/IP stack to alter outgoing packets and defeat Nmap fingerprinting.
Launching the program using the start.sh file will also give your computer a temporary MAC address and launch Chrome with a user agent matching your (spoofed) Nmap fingerprint.

***Development still in progress - use at your own risk.***

**For use on OSX 10.8.x**

*Planned features:*
* Additional profiles (Windows 8, Playstation/Xbox, Android)
* Wrap source as OSX app (py2app)

*Known issues:*
* Spoofed user agent OS and Nmap fingerprint OS don't dynamically match
* Nmap fingerprinting often results in an error (no OS found) rather than profile OS
