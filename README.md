# Selenium_DataScraping Notes

## The way of installing ChromeDriver has changed recently

Recently, Google published Chrome for Tester, so the method of install ChromeDriver has changed.
For versions 115 and newerStarting with M115 the ChromeDriver release process is integrated with that of Chrome. The latest Chrome + ChromeDriver releases per release channel (Stable, Beta, Dev, Canary) are available at the Chrome for Testing (CfT) availability dashboard. As a result, you might no longer have a need for version selection — you could choose any available CfT version and simply download the correspondingly-versioned ChromeDriver binary.

###*Reference*:
(https://sites.google.com/chromium.org/driver/downloads/version-selection?authuser=0)

(https://github.com/GoogleChromeLabs/chrome-for-testing#other-api-endpoints)

### *Chrome for Tester*
[The reason is shown here](https://developer.chrome.com/blog/chrome-for-testing/)

## The way to install Chrome Web Driver is now pretty easy:
The above is just to explain why the ChromeDriver has changed recently, and the way to install Chrome WebDriver is easy:
**In cmd window, type "npx @puppeteer/browsersinstallchrome@stable"**

### The code needs to install web_driver.manager:
pip install webdriver-manager

### To stop Selenium from closing the browser automatically, check this video
For some websites, they check if the requests come from the Browser Testing, which might reject the testing code. 
The options code at the beginning of the main.py file is used to workaround this problem.
https://www.youtube.com/watch?v=ijT2sLVdnPM

### Use XPath to find elements more precisely. You could refer to the reference 
[here](https://www.w3schools.com/xml/xpath_syntax.asp)