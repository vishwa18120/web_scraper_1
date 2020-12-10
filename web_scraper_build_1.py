import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np

#url of the page we want to scrape
url = "https://puzzel.org/en/wordseeker/play?p=-MNg3e7BaSDoTRef1qGj"
list = []
# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

#testhello

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all = soup.find('div',class_ = 'jsx-2110021720 WordSearchGrid grid')
letter = all.find_all('span',class_ = 'jsx-2615216660 Character')
for i in letter:
    list.append(i.text.lower())
# printing top ten job profiles
 # closing the webdriver
#driver.close()
list = np.array(list).reshape(20, 20)
print(list)
lines = []
count =0
with open("letters.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        lines.append(format(line.strip("\n")))

print(len(lines))
print(len(list))
print(len(list[0]))

for k in range(len(lines)):
    for i in range(20):
        for j in range(20):
            if list[i][j] == lines[k][0] and j + len(lines[k])-1 <20:
                c =0
                for l in range(len(lines[k])):
                    if list[i][j+l] == lines[k][l] :
                        c +=1
                if c == len(lines[k]):
                    print("Horizontal ",lines[k],f" {i},{j}")

            if list[i][j] == lines[k][0] and i + len(lines[k])-1 <20:
                c =0
                for l in range(len(lines[k])):
                    if list[i+l][j] == lines[k][l] :
                        c +=1
                if c == len(lines[k]):
                    print("Vertical ",lines[k],f" {i},{j}")
            if list[i][j] == lines[k][0] and j + len(lines[k])-1 <20 and i+ len(lines[k])-1 < 20:
                c =0
                for l in range(len(lines[k])):
                    if list[i+l][j+l] == lines[k][l] :
                        c +=1
                if c == len(lines[k]):
                    print("Rslide DOWN ", lines[k],f" {i},{j}")
            if list[i][j] == lines[k][0] and j + len(lines[k])-1 <20 and i- len(lines[k])-1 >= 0:
                c =0
                for l in range(len(lines[k])):
                    if list[i-l][j+l] == lines[k][l] :
                        c +=1
                if c == len(lines[k]):
                    print("Rslide UP", lines[k],f" {i},{j}")

            if list[i][j] == lines[k][0] and j - len(lines[k])-1 >= 0 and i - len(lines[k])-1 >=0:
                c =0
                for l in range(len(lines[k])):
                    if list[i-l][j-l] == lines[k][l] :
                        c +=1
                if c == len(lines[k]):
                    print("Lslide UP",lines[k],f" {i},{j}")
            if list[i][j] == lines[k][0] and j - len(lines[k])-1 >= 0 and i + len(lines[k])-1 < 20:
                c =0
                for l in range(len(lines[k])):
                    if list[i+l][j-l] == lines[k][l] :
                        c +=1
                if c == len(lines[k]):
                    print("Lslide DOWN",lines[k],f" {i},{j}")
