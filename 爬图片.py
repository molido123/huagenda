import re
from typing import final
def gethtml(url):
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  options=Options()
  options.add_argument('--headfull')
  options.add_argument("--disable-gpu")
  driver=webdriver.Chrome(executable_path="e://path mmm//chromedriver.exe",options=options)    
  driver.get(url)
  html=driver.page_source
  driver.close()
  driver.quit()
  return html

origin="https://findcumt.libsp.com/#/searchList/bookDetails/"
print("想看图？输入书的bookid")
add=input()
url=origin+add
html=gethtml(url)

example='><img src=("https://unicover.duxiu.com/coverNew/CoverNew.dll.iid=.+?") alt=""><p>图书</p></di'
picture_url=re.findall(example,html)
print(picture_url)