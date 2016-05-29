# Pioneer600

Pioneer600 sample program to control Raspberry pi with Joystick and monitor status on OLED of Pioneer600. 

Video Sample : https://youtu.be/f1ea1XTvkac 

Monitoring : 

  * Time / Date 
  * BMP180 infos - Temperature & Pressure & Altitude
  * Raspberry Pi Info 
	- CPU Temperature 
	- RAM Usage
	- CPU Usage
	- Disk Usage
  * IP Adresses 
  * Exchange Rates of TL (Turkish Lira & USD - EURO)
  * KODI Command (Kodi must be installed) 
  * System Command
	- Close this application
	- Restart Raspberry Pi
	- Shutdown system
	- Startx 
	- Application Update (app-get update and upgrade)
	- Raspberry Pi Kernel Upgrade rpi-update
	- Close App 


<b>To add on startup Raspberry pi</b>

sudo nano /etc/rc.local 

and add this line, change directore if you install differant location. 


<i>sudo python /home/pi/Pioneer600/Pioneer600.py &</i>



---------------

<b>Module </b>: Pioneer600
http://www.waveshare.com/wiki/Pioneer600

<b>Raspberry Pi </b>: B+ / 2B / 3B / Zero

<b>Language </b> Python 2 

--------------

<b>Used Pioneer600:</b>

  * LED sample
  * PCF8574 sample - Joystick
  * BMP180 sample programs- Barometer
  * OLED sample programs
  
----------------




