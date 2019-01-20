import tweepy
import mysql.connector
import time

consumer_key        =  'efrVX3g9v5wRLdafiPLt4DsvV'
consumer_secret     =  '5A3ldxUW0rvvPy8naJsMtuOniyiZkkp1PXWoTXuJeHPhe6waPa'
access_token        =  '983990687556427779-JaLmTSihAv920X2j4KNiEcMMSwAR5UZ'
access_token_secret =  '1vWIg4kI71EJY5GGIQtqibDLkcrNwrAyKDAnvt7z6OYNT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

me = api.get_user('compboi_')
fCount = me.followers_count

follow_list = []

while(True):
    followers = api.followers_ids('compboi_')
        
    for follower in followers:
        follower_info = api.get_user(follower).screen_name
        if follower_info not in follow_list:
            follow_list.append(follower_info)
            print ('Adding ' + follower_info + '.')
    time.sleep(61)