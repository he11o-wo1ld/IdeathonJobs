import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

url = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Greater%20Los%20Angeles%2C%20California%2C%20United%20States&locationId=&f_TPR=&distance=25&f_E=1%2C2&position=1&pageNum=0"

# location = input("Enter the location : ")
# designation = input("Enter your job preferences : ")

# loc = location.replace(" ", "%20")
# des = designation.replace(" ", "%20")
# des1 = des.replace(",", "%2C")
page = 1
# url = f"https://www.linkedin.com/jobs/search?keywords={loc}&location={des1}&f_TPR=&distance=25&f_E=1%2C2&position=1&pageNum={page}"



# def get_link_data(link):
#   response = requests.get(link)
#   print(response.status_code)
#   html = response.text
#   soup = bs(html, 'lxml')

#   typ = soup.find_all("span")[30]
#   return typ


def get_link(url):
    title = []
    links = []
    response = requests.get(url)
    print(response.status_code)
    html = response.text

    soup = bs(html, 'lxml')
    for link in soup.find_all('a', class_="base-card__full-link", attrs={'href': re.compile("^https://")}):
        # display the actual urls
        l = link.get('href')
        links.append(l)
    return links

  # for i in soup.find_all('h3', class_="base-search-card__title"):
  #   # print(i.text)
  #   pass

print(get_link(url))


# print(get_link(url))

