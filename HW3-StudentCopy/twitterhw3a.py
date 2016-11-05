# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy 

# Unique code from Twitter
access_token = "791350145665396738-MBz0iklydmOC8lBVbWOdANvCF8oGTb3"
access_token_secret = "i4KAiM3qO6FWltT8ZTzmCGdmc76zu5M0aORdhbxY03l9y"
consumer_key = "nRNVXexELjn4ZMSB5APdmnbnU"
consumer_secret = "fsPYlzDIcxeHy42fUV736nOqIoqo0fNI4BkENokc4h6sClIGS3"

# Boilerplate code here
# function to use the twitter API
def get_api():
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	return tweepy.API(auth)

#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
# api gets from Twitter
api = get_api()

#variable containing tweet information
tweet = "UMICH looking lovely as always #UMSI-206 #Proj3"

#path of the picture I want to upload
filename = '/Users/jules.wu/Desktop/Pic.jpg'

#uploads the tweet and picture onto Itwitter
status = api.update_with_media(filename, status = tweet)

print("Twitter Updated! Have a great day!")