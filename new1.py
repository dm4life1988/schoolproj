import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys 
from scapy.all import *

if len(sys.argv) !=4: # this takes the system argument which is the ip addrress which is target then the starting port
    #then the ending point there needs to be 3 arguments in total
    print ("usage: %s target startport endport" % (sys.argv[0])) # instructs the user to input 3 parameters
    sys.exit(0)

target = str(sys.argv[1]) # creates variables from the system argument first index is the IP address of the target
startport = int(sys.argv[2]) # this is the starting port to scan to see if its open creating the second index
endport = int(sys.argv[3]) # end point port also creating another index and the last one for the arguments
print ("Scanning " + target + " for open TCP ports\n") # scans the target for an open TCP port which is a range
# from the first port entered and the last port entered

if startport==endport:
    endport+=1
    
for x in range(startport,endport):
    packet = IP(dst=target)/TCP(dport=x,flags="S") #  # this is where the range is created to check and see if ports
    # are open in the desired range
    response = sr1(packet,timeout=0.5,verbose=0)   
    if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12: # this is checking the header in the packet for
        # the open port 0x12 which is the tcp handshake
        print ("Port "+str(x)+" is open!")
    sr(IP(dst=target)/TCP(dport=response.sport,flags="R"),timeout=0.5, verbose=0)

print ("Scan complete!\n")