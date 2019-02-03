import os
from time import sleep, strftime
from sys import platform

HOST = "www.google.com"
LOG = "log.txt"
TIMEOUT = 6;
INTERVAL = 2; #seconds b/w pings
COUNT = 3;    #num of packets to send

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
logFile.write("="*9)
logFile.write("Internet Logger started at "
              + strftime( "%Y/%m/%d ---- %H:%M:%S") )
logFile.write("="*9 + '\n')
wasUp = (os.system("ping -c " + str(COUNT) + ' ' + HOST +'&>/dev/null') == 0)
if wasUp:
    notify("Internet Up");
    logFile.write("internet UP at startup \n\n");
else:
    notify("Internet Down");
    logFile.write("internet DOWN at startup \n\n");
    
#continue checking
while 1:
    sleep(INTERVAL);
    response = os.system("ping -t " + str(TIMEOUT) +" -c " + str(COUNT) + ' ' + HOST+ '&>/dev/null')
    if response == 0 and not wasUp: 
        wasUp = True
        now = strftime("%Y/%m/%d ---- %H:%M:%S")
        logFile.write("internet went UP at " + now + '\n\n');
        notify("internet is now UP")
    elif response != 0 and wasUp:
        wasUp = False
        now = strftime("%Y/%m/%d ---- %H:%M:%S")
        logFile.close() 
        logFile = open(LOG, 'a')
        logFile.write("internet went DOWN at " + now + '\n\n');
        notify("internet is now DOWN")
        
