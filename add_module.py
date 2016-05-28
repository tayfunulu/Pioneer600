#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import socket
import fcntl
import struct
import urllib2
import xml.etree.ElementTree as ET
import urllib2

def kurnedir(sor):
	kurlar = {}
	tree = ET.parse(urllib2.urlopen('http://www.tcmb.gov.tr/kurlar/today.xml'))
	root = tree.getroot()

	for kurlars in root.findall('Currency'):
		Kod = kurlars.get('Kod')
		Unit = kurlars.find('Unit').text #    <Unit>1</Unit>
		isim = kurlars.find('Isim').text #    <Isim>ABD DOLARI</Isim>
    		CurrencyName = kurlars.find('CurrencyName').text #    <CurrencyName>US DOLLAR</CurrencyName>
    		ForexBuying = kurlars.find('ForexBuying').text #    <ForexBuying>2.9587</ForexBuying>
    		ForexSelling = kurlars.find('ForexSelling').text #    <ForexSelling>2.964</ForexSelling>
    		BanknoteBuying = kurlars.find('BanknoteBuying').text #    <BanknoteBuying>2.9566</BanknoteBuying>
    		BanknoteSelling = kurlars.find('BanknoteSelling').text #    <BanknoteSelling>2.9684</BanknoteSelling>
		CrossRateUSD = kurlars.find('CrossRateUSD').text #    <CrossRateUSD>1</CrossRateUSD>
		kurlar [Kod] = ForexBuying

	return kurlar[sor]

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try :
		ipnedir = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])
	except:
		ipnedir ="IP YOK"
	return ipnedir

# Return CPU temperature as a character string
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

# Return information about disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])
