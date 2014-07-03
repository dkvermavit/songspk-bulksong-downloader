'''
 :author: "Dharmendra Verma"
 :copyright: "Copyright 2013, Shopsense.Co" 
 :created: 03/07/14
 :email: "dharmendraverma@shopsense.co"   
 :github: @xrage 

'''
import urllib2


def url_resolver(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    res = opener.open(urllib2.Request(url))  # Resolve the redirects and gets the song Object
    return res, res.geturl()