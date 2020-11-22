# Go SMS Pro Scraper Demo
 Following the recent findings (Source: [Trustwave](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/go-sms-pro-vulnerable-to-media-file-theft/?=go-sms-pro-vulnerability-to-media-file-theft)) that the Android messaging app Go SMS Pro uploads all content publicly, here is an example of a scraper to fetch and download images from a URL following an incremental pattern.
 eg. site.example/000000 > FFFFFF

<br>

# Contribute
If you find this useful, please buy me a coffee

<a href="https://www.paypal.me/mattiab/">
    <img src="https://img.shields.io/badge/paypal-%2300457C.svg?&style=for-the-badge&logo=paypal&logoColor=white" />
</a>

<br>

 # WARNING
This tool is for ***research purpose only*** and retrieves content that is already public. Any action with any of the downloaded content is definitely against the law.

 # Setup
```
cd ~/Downloads
pip3 install requests
git clone https://github.com/mattiaborsoi/web-image-scraper
cd web-image-scraper
python scraper.py
```


 # Note 1
 I hope the developers fix the bug and implement some kind of authentication for shared content. Until then all attachments to a chat are exposed publicly.
 # Note 2
 The scraper in this example starts from the url URL/D/dd**0000**, increasing the HEX value to URL/D/dd**FFFF**
 

<p align='center'>
  <a href="#"><img src="https://badges.pufler.dev/visits/mattiaborsoi/web-image-scraper"></a>
</p>