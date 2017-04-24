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

<b>Details Installation:</b>
 
Fistly installing packaged which needed.

<i>
sudo apt-get install build-essential libi2c-dev i2c-tools python-dev libffi-dev

sudo pip install Image
</i>

And you have to enable spi, i2c, 1-Wire. There are two way, in terminal or application in desktop mode.
 
In terminal screen

<i>sudo raspi-config</i>
 
Under Advanced Option -> Enable SPI, I2C, 1-Wire
 
And restart….
 
to donwload codes from github 

git clone https://github.com/tayfunulu/Pioneer600.git
 
cd Pioneer600
 
To try
 
sudo python Pioneer600.py
 
to install kodi :

Sudo apt-get install kodi 
