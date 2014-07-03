'''
 :author: "Dharmendra Verma"
 :copyright: "Copyright 2013, Shopsense.Co" 
 :created: 03/07/14
 :email: "dharmendraverma@shopsense.co"   
 :github: @xrage 

'''

from bs4 import BeautifulSoup

class URLParserHref(object):
    @staticmethod
    def get_movie_names(url_data):
        soup = BeautifulSoup(url_data)
        data = soup.findAll('ul', attrs={'class' : 'ctlg-holder'})
        movie_list = []
        for div in data:
            links = div.findAll('a')
            for a in links:
                if a is not None and a is not "#":
                    movie_list.append(a.get('href', None))
        return movie_list

    @staticmethod
    def get_songs_url(song_data):
        song_list = []
        soup = BeautifulSoup(song_data)
        data = soup.findAll('a')
        for u in data:
            url = u.get('href', None)
            if url:
                if "songid=" in url:
                    song_list.append(url)
        return song_list

