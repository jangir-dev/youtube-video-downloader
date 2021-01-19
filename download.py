import sys
import youtube_dl

url = []

def download(link):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download(link)

try:
	url.append(sys.argv[1])
	download(url)
	if download(url):
		print("Successfully downloaded.")
except:
	print("Check the url")
	print("Syntax: python download.py link_of_video")