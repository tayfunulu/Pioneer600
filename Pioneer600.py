#!/usr/bin/python
# -*- coding:utf-8 -*-
# Tayfun ULU
import RPi.GPIO as GPIO
import smbus
import spidev as SPI
import SSD1306
import time
from BMP180 import BMP180
import Image
import ImageDraw
import ImageFont
import os
import fcntl
import struct
import add_module
from DovizKurlari import DovizKurlari

KEY = 20
address = 0x20
ana_menu = 1
son_menu = 1


def beep_on():
	bus.write_byte(address,0x7F&bus.read_byte(address))
def beep_off():
	bus.write_byte(address,0x80|bus.read_byte(address))
def led_off():
	bus.write_byte(address,0x10|bus.read_byte(address))
def led_on():
	bus.write_byte(address,0xEF&bus.read_byte(address))


def oled(bir,iki,ucst=""):
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top),str(bir), font=font1, fill=255)
        draw.text((x, top+20),str(iki), font=font2, fill=255)
	draw.text((x, top+40),str(ucst), font=font2, fill=255)
        disp.image(image)
        disp.display()

def MyInterrupt(KEY):
	print("KEY PRESS")

def menu ():
	global deger
	global son_menu
	global ana_menu

	if deger == "up" :
		son_menu = son_menu - 1
	elif deger == 'down' :
		son_menu =  son_menu + 1
	elif deger == "right" :
		ana_menu = ana_menu + 1
		son_menu = 1
	elif deger == "left" :
		ana_menu = ana_menu -1
		son_menu = 1

	if ana_menu == 8:
		ana_menu = 1
	if ana_menu == 0:
		ana_menu = 7

	#	if son_menu == 14:
	#		son_menu = 1
	#	if son_menu ==0:
	#		son_menu =13

	temp = bmp.read_temperature()
	pressure = bmp.read_pressure()
	altitude = bmp.read_altitude()

	#bilgiler
	if ana_menu == 1 :

		if son_menu == 3:
			son_menu = 1
		if son_menu ==0:
			son_menu =2

		if son_menu == 1:
			oled("<  1.Time   >",time.strftime('%X'))
		elif son_menu == 2 :
			oled("<  1.Date   >",time.strftime('%x'))

	# Sensor Verileri
	elif ana_menu == 2 :

		if son_menu == 4:
			son_menu = 1
		if son_menu ==0:
			son_menu =3

		if son_menu ==1:
			oled("< 2.Info >","Temperature",round(temp,2))
		elif son_menu ==2:
			oled("< 2.Info >","Pressure",round(pressure,2))
		elif son_menu ==3:
			oled("< 2.Info >","Altitude",round(altitude,2))

	# Cihaz bilgileri
	elif ana_menu == 3:

		if son_menu == 5:
			son_menu = 1
		if son_menu ==0:
			son_menu =4

		if son_menu == 1 :
			oled("< 3.Rpi Info >","CPU Temperature=",add_module.getCPUtemperature())
		elif son_menu == 2 :
			oled("< 3.Rpi Info >","RAM ",add_module.getDiskSpace()[3])
		elif son_menu == 3 :
			oled("< 3.Rpi Info >","CPU %",add_module.getCPUuse())
		elif son_menu == 4 :
			oled("< 3.Rpi Info >","Disk %",add_module.getDiskSpace()[3])
	# ipler
	elif ana_menu == 4 :

		if son_menu == 3:
			son_menu = 1
		if son_menu ==0:
			son_menu =2

		if son_menu == 1 :
			oled("< 4. Rpi IP's >","WLAN0",add_module.get_ip_address('wlan0'))
		elif son_menu == 2 :
			oled("< 4. Rpi IP's >","ETH0",add_module.get_ip_address('eth0'))

	#finansal
	elif ana_menu == 5 :

		if son_menu == 3:
			son_menu = 1
		if son_menu ==0:
			son_menu =2

		if son_menu == 1 :
			oled("< 5. Exch Rate >","Dolar / TL",DovizKurlari().DegerSor("USD",4))
		elif son_menu == 2 :
			oled("< 5. Exch Rate >","Euro / TL",DovizKurlari().DegerSor("EUR",4))

	#kodi
	elif ana_menu == 6 :

		if son_menu == 3:
			son_menu = 1
		if son_menu ==0:
			son_menu =2

		if son_menu == 1 :
			oled("< 6. KODI >","Open Kodi","Press Button")
			if GPIO.input(KEY) == 0:
				os.popen('sudo kodi &')

		elif son_menu == 2 :
			oled("< 6. KODI >","Close Kodi","Press Button")
			if GPIO.input(KEY) == 0:
				os.popen('sudo pkill kodi')

	#aç kapa
	elif ana_menu == 7 :

		if son_menu == 7:
			son_menu = 1
		if son_menu ==0:
			son_menu =6

		elif son_menu == 1 :
			oled("< 7. System >","Close App","Press Button")
			if GPIO.input(KEY) == 0:
				exit ()
		elif son_menu == 2 :
			oled("< 7. System >","Restart","Press Button")
			if GPIO.input(KEY) == 0:
				os.popen('sudo reboot')
		elif son_menu == 3 :
			oled("< 7. System >","Halt System","Press Button")
			if GPIO.input(KEY) == 0:
				os.popen('sudo halt')
		elif son_menu == 4 :
			oled("< 7. System >","Startx","Press Button")
			if GPIO.input(KEY) == 0:
				os.popen('startx &')
		elif son_menu == 5 :
			oled("< 7. System >","App Update","Press Button")
			if GPIO.input(KEY) == 0:
				oled("< 7. System >","Update ...")
				os.popen('sudo apt-get update')
				oled("< 7. System >","Upgrade ...")
				os.popen('sudo apt-get upgrade -y')
				oled("< 7. System >","Bitti")
		elif son_menu == 6 :
			oled("< 7. System >","Rpi Update","Press Button")
			if GPIO.input(KEY) == 0:
				oled("< 7. System >","Update ...")
				note=os.popen('sudo rpi-update')
				note = note.read()
				if note.find("Your firmware is already up to date") != -1 :
					oled("< 7. System >","Up to date")
					#print ("Güncel")
					time.sleep(1)
				else :
					oled("< 7. System >","Done")
					time.sleep(1)

	else :
		print ("wrong something")

	return (son_menu)

# Raspberry Pi pin configuration:
RST = 19
# Note the following are only used with SPI:
DC = 16
bus = 0
device = 0

# 128x64 display with hardware SPI:
disp = SSD1306.SSD1306(RST, DC, SPI.SpiDev(bus,device))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 1
top = padding
x = padding
# Load default font.
# font = ImageFont.load_default()
font_dir =  os.path.dirname(os.path.realpath(__file__)) +"/KeepCalm-Medium.ttf"
font1 = ImageFont.truetype(font_dir, 15)
font2 = ImageFont.truetype(font_dir, 14)

GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN,GPIO.PUD_UP)
#GPIO.add_event_detect(KEY,GPIO.FALLING,MyInterrupt,200)

bmp = BMP180()
bus = smbus.SMBus(1)

print("Pioneer600 Test Program !!!")
while True:
	bus.write_byte(address,0x0F|bus.read_byte(address))
	value = bus.read_byte(address) | 0xF0
	if value != 0xFF:
		led_on()
		if (value | 0xFE) != 0xFF:
			deger="left"
		elif (value | 0xFD) != 0xFF:
			deger="up"
		elif (value | 0xFB) != 0xFF:
			deger="down"
		else :
			deger="right"
		while value != 0xFF:
			bus.write_byte(address,0x0F|bus.read_byte(address))
			value = bus.read_byte(address) | 0xF0
			time.sleep(0.01)
		led_off()
		son_menu=menu()

	time.sleep(0.1)
	deger="YOK"
	son_menu=menu()
