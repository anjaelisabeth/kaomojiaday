#this bot posts a kaomoji a day to @kaomojiaday

import tweepy, time, requests
from bs4 import BeautifulSoup

#made them into variables in case I need to regenerate keys 
consumer_key = 'x7G0ZEg3wxXu2vc0fcHNM90z1'
secret_consumer_key = 'CONSUMER KEY GOES HERE'
access_token = 'ACCESS TOKEN GOES HERE'
secret_access_token = 'SECRET ACCESS TOKEN GOES HERE'

auth = tweepy.OAuthHandler(consumer_key, secret_consumer_key)
auth.set_access_token(access_token, secret_access_token)
myapi = tweepy.API(auth)

wiki = "https://en.wikipedia.org/wiki/List_of_emoticons"
soup = BeautifulSoup(requests.get(wiki).content, 'html.parser')
table = soup.find('table', class_="wikitable")
kaomoji = []
for row in table.find_all('th', scope='row'):
    kaomoji.append(row)
#print(kaomoji)

def add_kaomoji_to_file(kaomoji):
    #add kaomoji scraped from wikipedia into file used to send tweets
    file = open('kaomojilist.txt', 'r+', encoding='UTF-8')
    for i in kaomoji:
        file.write("%s\n" % i)
    file.close()
        

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
    
#def main():
    #send_kaomoji_tweets()
    #follow_back()

#main()
#myapi.update_profile_image('kaomojprofpic.jpg')

   
