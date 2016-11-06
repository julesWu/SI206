# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "791350145665396738-MBz0iklydmOC8lBVbWOdANvCF8oGTb3"
access_token_secret = "i4KAiM3qO6FWltT8ZTzmCGdmc76zu5M0aORdhbxY03l9y"
consumer_key = "nRNVXexELjn4ZMSB5APdmnbnU"
consumer_secret = "fsPYlzDIcxeHy42fUV736nOqIoqo0fNI4BkENokc4h6sClIGS3"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

#prompts user for search term
search_term = input("What term would you like to search: ")

#searches twitter for the search_term
public_tweets = api.search(search_term)

#initialize count for subjectivity to 0
total_subj = 0

#initialize count for polarity to 0
total_polar = 0

#a for loop to iterate through the tweets in public_tweets
for tweet in public_tweets:
	#prints out the tweet
	print(tweet.text)
	#analyzes the tweet for sentiments
	analysis = TextBlob(tweet.text)
	#adds the subjectivity of the tweet to total_subj
	total_subj += analysis.sentiment.subjectivity
	#adds the polarity of the tweet to total_polar
	total_polar += analysis.sentiment.polarity
	
#outputs the average subjectivity and average polarity
print("Average subjectivity is", end = " ")
print (total_subj / len(public_tweets))
print("Average polarity is", end = " ")
print (total_polar / len(public_tweets))


	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

