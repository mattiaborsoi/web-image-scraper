# Go SMS Pro Scraper
 Following the recent findings (Source: [Trustwave](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/go-sms-pro-vulnerable-to-media-file-theft/?=go-sms-pro-vulnerability-to-media-file-theft)) that the Android messaging app Go SMS Pro uploads all content publicly, here is a quick scraper to fetch and download all publicly available content.

<br>

# Contribute
If you find this useful, please buy me a coffee

<a href="https://www.paypal.me/mattiab/">
    <img src="https://img.shields.io/badge/paypal-%2300457C.svg?&style=for-the-badge&logo=paypal&logoColor=white" />
  </a>

<br>

 # WARNING
This tool is for research purpose only and retrieves content that is already public. Any action with any of the downloaded content is against the law.

 # Setup
```
pip3 install wget
git clone https://github.com/mattiaborsoi/Go-SMS-Pro-Scraper
cd Go-SMS-Pro-Scraper
sh sms.sh
```


 # Note
 1 - the links may be revoked at anytime should the developer fix the bug. 
 <br>
 2 -  The scraper starts from the url http://gs.3g.cn/D/dd**0000**, increasing the HEX value to http://gs.3g.cn/D/dd**FFFF**
 You can edit that URL to http://gs.3g.cn/D/**00** in the code to scrape ALL the available content


<p align='center'>
  <a href="#"><img src="https://badges.pufler.dev/visits/mattiaborsoi/mattiaborsoi"></a>
</p>