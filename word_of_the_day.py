import os
from bs4 import BeautifulSoup
import urllib2

BASE_URL = 'http://www.wordthink.com/'

def main():
    word = get_word()
    para = get_information_about_word(word)
    print para
    
    with open("Words of day.txt","a") as f:
        f.write(str(para)+"\n\n\n")
    
    notif='notify-send -i /home/varun/Desktop/word.png "'+word+'" "'+str(para)+'"'
    os.system(notif)

def get_word():
    page = urllib2.urlopen(BASE_URL)
    soup = BeautifulSoup(page.read())
    what = soup.find("h2", {"class": "title"})
    word = what.a.contents[0] #Got word
    return word

def get_information_about_word(word):
    url = BASE_URL + word
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    para = soup.find('p').getText()
    para = para.encode('ascii',errors='ignore') #removes non ascii characters

if __name__ == '__main__':
  main()
