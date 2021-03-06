from twython import *
import configparser
import sys
import os
from datetime import timedelta

# Read configuration
configuration = {}
try:
    config = configparser.ConfigParser()
    absPath = os.path.dirname(os.path.abspath(__file__)) + '/config/'
    config.read([absPath + 'config.ini', absPath + 'autotweet.ini'])

    # Read all options into a dictionary
    for section in config.sections():
        configuration[section] = {}
        for option in config.options(section):
            configuration[section][option] = config.get(section, option)

except configparser.MissingSectionHeaderError as e:
    print("Could not read configuration. Exiting")
    exit()

# Instantiate Twitter API with credentials
oauth = configuration['OAuth']
twitter = Twython(oauth['app_key'], oauth['app_secret'], oauth['oauth_token'], oauth['oauth_token_secret'])

# Get uptime
uptimeValue = 'Unknown.'

try:
    with open('/proc/uptime', 'r') as f:
        uptimeSeconds = float(f.readline().split()[0])
        uptimeValue = str(timedelta(seconds=uptimeSeconds))
except IOError:
    print("Cannot tweet uptime, not on a Pi.")

# Get current time
from time import localtime, strftime
currentTime = strftime("%d.%m.%Y %H:%M:%S", localtime())

# Try to tweet
if 2 == len(sys.argv):
    # Tweet and inject the uname
    mode = int(sys.argv[1])
    tweet = ''
    if mode == 1:
        # Boot
        tweet = configuration['Autotweet']['boot_message']
    elif mode == 0:
        # Shutdown
        tweet = configuration['Autotweet']['shutdown_message']
    else:
        tweet = 'Unknown Mode was used when starting {0}'
    tweet = tweet.format(os.uname()[1], uptimeValue, currentTime)
    try:
        twitter.update_status(status=tweet)
    except TwythonError as Error:
        print("Could not authenticate with the Twitter API. Your API is probably set to Read-Only.")
        print(format(Error))
else:
    print("Did not receive a parameter. Exiting.")
    exit()