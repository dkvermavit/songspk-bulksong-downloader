from sgmllib import SGMLParser
import urllib, urllib2
import sys
try:
	import eyed3
except:
	print "eyed3 in not installed, Songs title will not be renamed properly, or some songs overwrite problems my occur"
	user_in = input('Press 1 to continue or 2 to exit')
	if user_in != 1:
		sys.exit(0)

import os


class URLLister(SGMLParser):

    def reset(self):                              
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):                     
        href = [v for k, v in attrs if k=='href']  
        if href:
            self.urls.extend(href)



class SongsPK:
	def __init__(self):
		dirpath = os.path.expanduser('~/Desktop/songsPK_Collection')
		if not os.path.exists(dirpath):
			os.system('mkdir %s' %dirpath)
		self.dirpath = dirpath

	def write_MP3(self, mp3):
		"""
		Writes the downloaded file and renames the title.
		"""
		name = (mp3.geturl()).split('/')
		folder_name = os.path.expanduser(self.dirpath+'/'+name[-3]+'/')
		song_name = name[-2]+name[-1]

		if not os.path.exists(folder_name):
			os.system('mkdir %s' %folder_name) # Creates a directory on current users Desktop
		#File Opening and writing
		fullpath = folder_name+song_name
		with open(fullpath,'w') as output:
			while True:
				buf = mp3.read(65536)
				if not buf:
					break
				output.write(buf)
		try:
			audiofile = eyed3.load(fullpath)  #eyed3 module used for changing the audio file properties.
			if audiofile.tag.title:
				os.rename(fullpath, folder_name+audiofile.tag.title)
		except Exception as e:
			print "Not able to edit title"
			pass


	def Urlbased(self, url_datas=None):
		visited_url = []
		parser = URLLister()
		if not url_datas:
			url_datas = raw_input("Enter comma separated url strings\n")
		url_datas = url_datas.split(',')
		url_count = 0
		for url_data in url_datas:
			if url_data.startswith('www'):
				url_data = url_data.replace('www', 'http://www')
			usock = urllib.urlopen(url_data)
			parser.feed(usock.read()) 
			usock.close()      
			parser.close()
			url_count+=1
			parse_url = 0
			for url in parser.urls:
				parse_url+=1
				try:
					req = urllib2.Request(url)
					res = urllib2.urlopen(req)
					finalurl = res.geturl()
					if finalurl.endswith('.mp3') and finalurl not in visited_url and not finalurl.startswith('..'):
						self.write_MP3(res)
					visited_url.append(finalurl)
				except Exception as e:
					print e.message
					continue
				print str(int(parse_url*100)/len(parser.urls)) + "percent songs processed of url --->" + str(url_count)


	def movieHandler(self):
		movie_letter = raw_input('Enter Indian Movie start letter [A-Z] to get movie name list\n')
		parser = URLLister()
		usock = urllib.urlopen('http://songspk.info/indian_movie/%s_List.html' %movie_letter.upper())
		parser.feed(usock.read()) 
		usock.close()      
		parser.close()
		url_dict = {}
		count = 1
		for url in parser.urls:
			if not url.startswith('..'):
				url_dict[str(count)] = url
				count+=1
		for k ,v in url_dict.iteritems():
			print k + '-----' + v.rstrip('.html')

		movie = raw_input('Enter movie number to download all songs of it\n')
		movie_url = "http://songspk.info/indian_movie/%s" %url_dict[movie]
		self.Urlbased(url_datas=movie_url)




if __name__ == "__main__":
	handle = SongsPK()
	print "Please select an option to proceed\n"
	print "1 - Url based bulk song download\n"
	print "2 - Movie name based bulk song download\n"
	while True:
		option = input('Enter your option {1 or 2}\n')
		if option == 1:
			handle.Urlbased()
			break
		elif option == 2:
			handle.movieHandler()
			break
		else:
			print "Invalid option"
			continue
