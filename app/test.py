#! /usr/bin/env python

import sys
import time
from scapy.all import sr1,IP,ICMP, TCP, send
from pymongo import MongoClient
from random import randint

ttl = time.time() + 60*int(sys.argv[3]);
while 1:
    if time.time() > ttl:
        break


