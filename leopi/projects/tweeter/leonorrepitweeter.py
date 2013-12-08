from twython import *
import configparser

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

# Check if we want to tweet something
tweet = input("Please enter a message to tweet, or leave empty if you don\'t want to tweet at this time:")
if 0 < len(tweet):
    try:
        twitter.update_status(status=tweet)
        print("Successfully tweeted", tweet)
    except TwythonError as Error:
        print("Could not authenticate with the Twitter API. Your API is probably set to Read-Only.")
        print(format(Error))
else:
    print("Not tweeting anything.")


# Cleanup
del tweet


# Delete last tweet
delete = int(input("Enter the number of last tweets you wish to delete:"))
if 0 < delete:
    timeline = twitter.get_home_timeline()
    counter = len(timeline)

    if delete > counter:
       print("Cannot delete more items than are in the timeline. Not deleting anything.")
    else:
        counter = 0
    while delete > 0:

        # Get tweet id
        tweet = timeline[counter]
        tweetId = tweet['id_str']
        tweetText = tweet['text']

        # Perform delete action
        twitter.destroy_status(id=tweetId)

        # Notify
        print("Deleted the tweet with the text '", tweetText, "'", sep="")

        # Increment
        counter += 1
        delete -= 1
else:
    print("Not deleting anything.")