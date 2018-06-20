
#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)

white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
yellow = '\033[1;33m'
end = '\033[1;m'
info = '\033[1;33m[#]\033[1;m'
que =  '\033[1;34m[>]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'
run = '\033[1;97m[~]\033[1;m'

print '''\033[1;32m
   ____     
|V/    \   T u F      _  ____   _______
|   D   |   ____     | |/___ \ |__   __|
|  ____/   / __ \    | |V   \_\   | |
| |       | /  \ |   | |          | |
| |       | \__/ |   | |          | |
|_|        \____/    |_| SCANNER  |_|
Created By : @un_kn0wn_h4c_k3r on instagram
Also  Follow : @tuf_boss on instagram \033[1;m'''

# Ask for input
remoteServer    = raw_input('\033[1;34m>\033[1;m \033[1;33m Enter the target: \033[1;m')
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "\033[1;31m-\033[1;m" * 60
print "\033[1;32m Please wait, scanning Target \033[1;m", remoteServerIP
print "follow \033[1;32m un_kn0wn_h4c_k3r \033[1;32m and \033[1;32m tuff_boss on instagram \033[1;m"
print "\033[1;31m-\033[1;m" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "\033[1;34m Port {}: 	 Open \033[1;m".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print '\033[1;32m Target Scanned in: \033[1;m', total
