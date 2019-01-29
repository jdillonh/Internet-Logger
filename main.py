import os
from time import sleep, strftime
from sys import platform

HOST = "www.google.com"
LOG = "log.txt"
INTERVAL = 2; #seconds b/w pings
COUNT = 2;    #num of packets to send

if platform == 'darwin':
    def notify(m):
        """display a handy notification on the desktop"""
        os.system("osascript -e 'display notification \"Internet Logger says: " + m + "\"'");
else:
    def notify(m):
        """Insert you desktop environment notification code here"""
        pass

# startup routine
logFile = open(LOG, 'a');
logFile.write("Internet Logger started at "
              + strftime( "%Y/%m/%d ---- %H:%M:%S") + '\n')
wasUp = (os.system("ping -c " + str(COUNT) + ' ' + HOST +'&>/dev/null') == 0)
if wasUp:
    logFile.write("internet UP at startup \n");
    notify("Internet Up");
else:
    notify("Internet Down");
    logFile.write("internet DOWN at startup \n\n");
    
#continue checking
while 1:
    sleep(INTERVAL);
    response = os.system("ping -c " + str(COUNT) + ' ' + HOST+ '&>/dev/null')
    if response == 0 and not wasUp:  #it's up :)
        wasUp = True
        now = strftime("%Y/%m/%d ---- %H:%M:%S")
        logFile.write("internet went UP at " + now + '\n\n');

    elif response != 0 and wasUp:
        wasUp = false
        now = strftime("%Y/%m/%d ---- %H:%M:%S")
        logFile.write("internet went DOWN at " + now + '\n\n');
        
