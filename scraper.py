import sys
import requests
import urllib.parse
import wget
site = sys.argv[1]
print(site)
r = requests.get(site)
imageUrl=r.url

imageUrl = imageUrl.replace('http://gosms.gomocdn.com/mms/v14/index.html?u=', "")
imageUrl = urllib.parse.unquote_plus(imageUrl)
imageUrl = imageUrl.rsplit('&')[0]
local_image_filename = wget.download(imageUrl)