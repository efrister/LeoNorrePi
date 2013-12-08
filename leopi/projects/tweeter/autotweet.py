from twython import *
import configparser
import sys

# Read configuration
configuration = {}
try:
    config = configparser.ConfigParser()
    config.read('config.ini')

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

if 2 == len(sys.argv):
    tweet = sys.argv[1]
    try:
        twitter.update_status(status=tweet)
    except TwythonError as Error:
        print("Could not authenticate with the Twitter API. Your API is probably set to Read-Only.")
        print(format(Error))
else:
    print("Did not receive a parameter. Exiting.")
    exit()