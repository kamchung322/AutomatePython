import requests, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver import Firefox

def displaySummary():
    print("webbrowser Comes with Python and opens a browser to a specific page.")
    print("See Ch12-mapIt.py for sample")
    print("requests Downloads files and web pages from the internet.")
    print("bs4 Parses HTML, the format that web pages are written in.")
    print("See Ch12-searchPypi.py for sample")
    print("selenium Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.")
    print("requests and bs4 can manipulate web page without open browser")
    print("selenium simulate human being to open browser")

def downloadFile():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    print(res.status_code == requests.codes.ok)
    print(res.text[:250])

def downloadFileError():
    res = requests.get('https://automatetheboringstuff.com/non_exist_file.txt')
    try:
        res.raise_for_status() # Raise error If cannot download file
    except Exception as exc:
        print("There was a error : %s " %exc)

def saveDownloadedFile():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    savedFile = open(r"C:\TEMP\rj.txt", "wb")

    for chunk in res.iter_content(100000):
        savedFile.write(chunk)
    
    savedFile.close()

def checkMyUA():
    res = requests.get('https://www.whatsmyua.info/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    uaText = soup.find("textarea", {"id": "custom-ua-string"})
    #soup.find("div", {"id": "articlebody"})
    print(uaText)

def loginSpamTitan():
    # https://automatetheboringstuff.com/2e/chapter12/
    # https://selenium-python.readthedocs.org/

    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
    browser.get("http://192.168.0.22/login.php")
    userName = browser.find_element_by_id("address")
    userName.send_keys("admin")
    passwd = browser.find_element_by_id("passwd")
    passwd.send_keys("namwah168")
    btnOK = browser.find_element_by_id("loginButton")
    btnOK.submit()
    #browser.get("http://192.168.0.22/manage-quarantine.php")

def play2048():
    # keep sending up, right, down, and left 
    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
    browser.get("https://play2048.co/")
    htmlElem = browser.find_element_by_tag_name("html")
    
    for i in range(1000):
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.DOWN)


play2048()
#loginSpamTitan()
#checkMyUA()
#saveDownloadedFile()
#downloadFileError()
#downloadFile()
#displaySummary()