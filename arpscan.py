from scapy.all import srp,ARP,Ether,conf
import sys
from datetime import datetime

try:
    interface = raw_input("[*] Enter Desired Interface: ")
    ips = raw_input("[*] Enter IP range to scan : ")

except KeyboardInterrupt:
    print "\n[*] Quiting......"
    sys.exit(1)


print "[*] Scanning.......\n"
time1 = datetime.now()  # when the scan start

conf.verb = 0  #Actually start scanning
ans , unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips) , timeout=2 , iface=interface , inter=0.1)

print "    MAC Address   - IP Address\n"
for snd,rcv in ans:
    print rcv.sprintf(r"%Ether.src% - %ARP.psrc%")

time2 = datetime.now()   # when the scan finished
scan_time = time2 - time1  # time that was taken to finish the scan

print "\n[*] Scan Complete!"
print ("[*] Scan Duration: %s" %(scan_time))
