__author__ = 'edgar'

import dpkt
from sys import argv
from scapy.all import *
import time


script, filename = argv;

""" Doesn't work :(
logFile = open(filename, 'r');

while 1:
    where = logFile.tell();
    line = logFile.readline();

    if not line:
        time.sleep(1);
        logFile.seek(where);
    else:
        ts, pkt = dpkt.pcap.Reader(line);
        print ts, len(pkt);
        # parse here
        # I.E. update all values here
        # Place parser here and call it to parse data
"""
# To start it off
pkts = rdpcap(filename);
outpkts = [];
start = 0;
end = len(pkts)-1;

while 1:
    while( start <= end ):
        # Do parsing right here....
        #outpkts.append(pkts[start]);
        #print( "Packet: %s" % (pkts[start])[0][1].src);
        (pkts[start])[0][1].show();
        start += 1;



    # Update start & end to include newly generated packets in log file
    pkts = rdpcap(filename); # Open updated
    start = end;
    end = len(pkts)-1;