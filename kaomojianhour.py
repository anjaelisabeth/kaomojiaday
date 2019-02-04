#this bot posts a kaomoji a day to @kaomojiaday


import tweepy, time, wikipedia
from bs4 import BeautifulSoup

#made them into variables in case I need to regenerate keys 
consumer_key = 'x7G0ZEg3wxXu2vc0fcHNM90z1'
secret_consumer_key = 'Y30mnZvhOyKTFLXSLP9nsGGDfX7UyWWZoFT6HMPHI2wPsPVkBk'
access_token = '1092225188329066496-u2xQz6V9z5gv7biCZ0LSulwMJGwg9m'
secret_access_token = 'm72plBHoTrG8QZ2ChKQ6VRiuQZenRjSFyXNE3bHf54uRm'

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
    time.sleep(30)
    
def main():
    send_kaomoji_tweets()
    while True:
        follow_back()
main()
#myapi.update_profile_image('kaomojprofpic.jpg')

    


