import RPi.GPIO as GPIO
from time import time,strftime

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7

GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    currentTime = strftime("%d.%m.%Y %H:%M:%S")
    print("Motion Detected at ", currentTime)

print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)

print("Ready")

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=MOTION)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()