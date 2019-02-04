#this bot posts a kaomoji a day to @kaomojiaday


import tweepy, time, wikipedia
from bs4 import BeautifulSoup

#made them into variables in case I need to regenerate keys 
consumer_key = 'CONSUMER_KEY'
secret_consumer_key = 'SECRET_CONSUMER_KEY'
access_token = 'ACCESS_TOKEN'
secret_access_token = 'SECRET_ACCESS_TOKEN'

auth = tweepy.OAuthHandler(consumer_key, secret_consumer_key)
auth.set_access_token(access_token, secret_access_token)
myapi = tweepy.API(auth)

def send_kaomoji_tweets():
    file = open('kaomojilist.txt', 'r+', encoding='UTF-8')
    lines = file.readlines()
    for line in lines:
        myapi.update_status(line)
        time.sleep(43200)
    file.close()

def follow_back():
    followers = myapi.followers()
    for follower in followers:
        follower.follow()
    
def main():
    send_kaomoji_tweets()
    follow_back()

main()
#myapi.update_profile_image('kaomojprofpic.jpg')

    


