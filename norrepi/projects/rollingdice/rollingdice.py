import random
import time


def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        print('Please install ' + module_name + ', see more here.')
    else:
        return True

if module_exists('random'):
    Freq = 2500 # Set Frequency To 2500 Hertz
    Dur = 1000 # Set Duration To 1000 ms == 1 second

    diceValue = random.randint(1, 6)

    print(diceValue)

    for x in range(0, diceValue):
        time.sleep(0.5)
        print('\a')