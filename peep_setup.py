import tweepy
import time

api_key = "ZXzFqyDrDtymtKOZ7vm6U17Eu"
api_secret = "F9mCMrmSNDiVxZilHMYd0hvJiE2sMNJ6tyeLPFha41m8F3vLsE"
bearer_token = "AAAAAAAAAAAAAAAAAAAAALkmugEAAAAASVR8ITozqppNaet8QOJDd5T6ktA%3DBtz8ixD6ZUfevZ34SJ7cEM6TS6uBfjEF4f7Y0AsR9dd3m6C8bY"
access_token = "1806254121051148288-zWjjEcWBDDqImMii3sgpCCrctazT4Y"
access_token_secret = "WHX7Wb0GPtnrXLmMPjL2KlbLpReNJLQcMK8pjcaFPijvd"

client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)

auth = tweepy.Client(bearer_token, api_key, api_secret,access_token, access_token_secret)
api = tweepy.API(auth)


# client.create_tweet(text="Hello Twitter")

# client.like(1806262774118453570)

#client.retweet(1806262774118453570)

#client.create_tweet(in_reply_to_tweet_id=1806262774118453570, text="Hello user")

#for tweet in api.home_timeline(): #tweets in home timeline
    #print(tweet.text)

#person = client.get_user(username="NishaSingh55002").data.id

#for tweet in client.get_users_tweets(person).data:  
    #print(tweet.text)

search_terms = ["python", "programming", "coding"]

class MyStream(tweepy.StreamingClient): #this function will run once the stram comes alive and starts
    def on_connect(self):
        print("Connected") #other than all the on tweet function is the best which basically gets called oncce the stream detects a tweet which matches the filter criteria.

    def on_tweet(self, tweet): # is has a property called referenced tweets which basically stores information which determines if a certain tweet is a retweet or a reply if this reference tweet's property
        if tweet.references_tweets == None:
            print(tweet.text)

            time.sleep(0.2) #this will delay in seconds so that we will not get bombarded with tweets

stream = MyStream(bearer_token=bearer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter() #it will start filtering
# now evern with this line of code here we are stil going to receinve tweets which are retweets or replies
#the reason behin this is that the stream doesn't yet have access to  referenced tweet property so we are gonna give access down here by passing an argument to a parameter

stream.filter(tweet_fields=["referenced_tweets"])

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)

        except Exception as error:
            print(error)


stream = MyStream(bearer_token=bearer_token)

#stream rule are the basic rules which follow basic stream which tweets we want

rule = tweepy.StreamRule("#Pyton OR #programming (-is: retweet -is:reply)") # now it will show all pyhotn ones

stream.add_rules(rule, dry_run=True)

stream.add_rules(rule)

stream.filter()