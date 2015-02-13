from flask import Flask, request, render_template
app = Flask(__name__)

import tweepy
import urllib
import helpers


# !!!!!!!!!!!! FILL THESE OUT BEFORE RUNNING THE APP !!!!!!!!!!!!!!!! 
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

WTF_CSRF_ENABLED = True

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route('/')
def home_search():
	return render_template('home.html')

@app.route('/memeified/', methods=['POST'])
def handle_query():
	# get parameters passed into form on home page.
	# !!!
	# !!!
	
	# format the text to apimeme.com's liking
	# !!!

	# Use tweepy to make a REST call to search for a twitter user with the query the user entered
	# !!! 
	# we're just going to assume that Twitter's search got this right and the first user is the one we want. 
	# !!!

	# Use tweepy to make a REST call to get this user's timeline of tweets
	# !!! tweets = 
	# Get the most recent tweet from the api and get it's text
	# !!! tweet = 

	# split the tweet into top and bottom text through our helper function
	# top_text, bottom_text = helpers.get_meme_text_from_tweet(tweet)
	
	# construct apimeme.com url from top and bottom text
	# !!!
	# return render_template('memeify.html', image_src=image_url, twitter_user=user.screen_name)
	
	return "Im not complete..."
	

if __name__ == '__main__':
	app.run(debug = True)
