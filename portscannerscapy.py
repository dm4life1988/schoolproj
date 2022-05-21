from scapy.all import IP, sr1, TCP

OPEN_PORTS = []

def analyze_port(host,port):
    # Host is the host to target to scan 
    # port to test use integer
    print("[ii] Scanning port %s" % port)
    res = sr1(IP(dst=host)/TCP(dport=port),verbose=False, timeout=0.2)
    if res is not None and TCP in res:
        if res[TCP].flags == 18:
            OPEN_PORTS.append(port)
            print("Port %s open" % port)
def main():
    for x in range(0,80):
        analyze_port("domain", x)
    print("[*] Open Ports:")
    for x in OPEN_PORTS:
        print("-%s/TCP" % x)