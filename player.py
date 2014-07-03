'''
 :author: "Dharmendra Verma"
 :copyright: "Copyright 2013, Shopsense.Co" 
 :created: 03/07/14
 :email: "dharmendraverma@shopsense.co"   
 :github: @xrage 

'''

import subprocess
import sys
from utils import url_resolver


class Player(object):

    @staticmethod
    def _check_mpg123():
        try:
            subprocess.call('mpg123 --version')
        except OSError:
            print 10*"#\n"+"Please install mpg123 to enable play mode"+"\n#"*10
            sys.exit()

    @staticmethod
    def play(song_url):
        try:
            subprocess.call("mpg123 %s" %url_resolver(song_url)[1])
        except:
            print "Failed in playing from url %s" %song_url




