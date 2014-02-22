import RPi.GPIO as GPIO
import time
from time import strftime

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 7
EVENT_FALLING = "FALLING"
EVENT_RISING = "RISING"

GPIO.setup(PIR_PIN, GPIO.IN)

last_event = ""

def MOTION(PIR_PIN):
    current_time = strftime("%d.%m.%Y %H:%M:%S")
    current_event = ""
    if last_event == "" or last_event == EVENT_FALLING:
        current_event = EVENT_RISING
    else:
        current_event = EVENT_FALLING

    if current_event == EVENT_RISING:
        msg = "Motion detected"
    else:
        msg = "PIR stopped sending last motion. Ready for next event"

    last_event = current_event
    print(msg, "at", current_time)

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