# This program uses Tweepy to extract tweet details of a hashtag input
# Prints tweets AND saves it to a CSV file
import pandas as pd
import tweepy
from tweepy import OAuthHandler

# Function to perform data extraction
def extract(tag, date_to, numtweet):
	
	# Pandas DataFrame
	df = pd.DataFrame(columns=['username', 'description', 'location', 'following',
							'followers', 'totaltweets', 'retweetcount', 'text', 'hashtags'])
	
	# Searching Tweets
	tweets = tweepy.Cursor(api.search, q=tag, lang="en",
						since=date_to, tweet_mode='extended').items(numtweet)
	
	list_tweets = [tweet for tweet in tweets]
	i = 1 # Tweet Count
	
	# Extracting info of tweets
	for tweet in list_tweets:
		username = tweet.user.screen_name
		description = tweet.user.description
		location = tweet.user.location
		following = tweet.user.friends_count
		followers = tweet.user.followers_count
		totaltweets = tweet.user.statuses_count
		retweetcount = tweet.retweet_count
		hashtags = tweet.entities['hashtags']
		
		# Exception used for "Invalid references"
		try:
			text = tweet.retweeted_status.full_text
		except AttributeError:
			text = tweet.full_text
		hashtext = list()
		for j in range(0, len(hashtags)):
			hashtext.append(hashtags[j]['text'])
		
		# Append tweets to DataFrame
		ith_tweet = [username, description, location, following,
					followers, totaltweets, retweetcount, text, hashtext]
		df.loc[len(df)] = ith_tweet
		
		# Print tweet data function
		displaytweets(i, ith_tweet)
		i = i+1
    # Save all hashtag findings to CSV file    
	filename = 'tweepy_extract.csv'
	df.to_csv(filename)

# Function to print data of each tweet
def displaytweets(n, tweet):
	print()
	print(f"Tweet {n}:")
	print(f"Username:{tweet[0]}")
	print(f"Description:{tweet[1]}")
	print(f"Location:{tweet[2]}")
	print(f"Following:{tweet[3]}")
	print(f"Followers:{tweet[4]}")
	print(f"Total Tweets:{tweet[5]}")
	print(f"Retweet Count:{tweet[6]}")
	print(f"Tweet Text:{tweet[7]}")
	print(f"Other hashtags:{tweet[8]}")

if __name__ == '__main__':
	
	# Consumer keys and access tokens, used for OAuth
	consumer_key = "kbjS8vAFrE3j4KYWl2A6FlkJ2"
	consumer_secret = "dibrWSwgeryIW1KQ3mEL6yX4qhAwwASJYHGvL16scXGn6JuhU9"
	access_key = "2380741826-mQ5MsqlfWLfVuqGYRrv2XovdbVZDm1FjoGG6Qx2"
	access_secret = "d4B7hR536q5QEEMYYOjphHQF614MTfPQo58tF7xBXPpd7"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

    # Enter Hashtag and initial date
	print("Enter the hashtag you want to extract:")
	tag = input()
	print("Enter from how long ago you want to extract (In 'yyyy-mm--dd'):")
	date_to = input()
	
	numtweet = 10  # numtweet can be adjusted to how many tweets you want to gather per execution
	extract(tag, date_to, numtweet)
	print('Twitter Scraping Complete.') 