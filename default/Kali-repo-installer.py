import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24 ,GPIO.OUT)
GPIO.setup(23 ,GPIO.IN)

GPIO.output(24,1)


print("+------------------------------!!!  WARNING  !!!------------------------------+")
print("|          This operation will modifiy your /etc/apt/sources.list.d           |")
print("|                 press any key on your IR remote to confirm                  |")
print("+-----------------------------------------------------------------------------+")


while 1==1:
    if GPIO.input(23) == 0:
        os.system('touch /etc/apt/sources.list.d/kali.list')
        os.system('sudo echo "deb [trusted=yes] http://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list.d/kali.list')
        os.system('wget -q -O - archive.kali.org/archive-key.asc | apt-key add')
        os.system("sudo apt-get update --allow-unauthenticated")
        break
