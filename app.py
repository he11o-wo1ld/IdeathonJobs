import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_data():
      page = 1
      limit = 10
      while page <= limit:
            url = f"https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Greater%20Los%20Angeles%2C%20California%2C%20United%20States&locationId=&f_TPR=&distance=25&f_E=1%2C2&position=1&page={page}"

            # location = input("Enter the location : ")
            # designation = input("Enter your job preferences : ")

            # loc = location.replace(" ", "%20")
            # des = designation.replace(" ", "%20")
            # des1 = des.replace(",", "%2C")
            # url = f"https://www.linkedin.com/jobs/search?keywords={loc}&location={des1}&f_TPR=&distance=25&f_E=1%2C2&position=1&pageNum={page}"



            # def get_link_data(link):
            #   response = requests.get(link)
            #   print(response.status_code)
            #   html = response.text
            #   soup = bs(html, 'lxml')

            #   typ = soup.find_all("span")[30]
            #   return typ
            JobData = []
            title = []
            links = []
            response = requests.get(url)
            html = response.text

            soup = bs(html, 'lxml')
            for link in soup.find_all('a', class_="base-card__full-link", attrs={'href': re.compile("^https://")}):
                  # display the actual urls
                  l = link.get('href')
                  links.append(l)

            for i in soup.find_all('h3', class_="base-search-card__title"):
                  td = i.text.replace('\n', '')
                  title.append(td.replace(' ', ''))
            
            page += 1
            
      for i in range(len(title)):
            data = {}
            data['title'] = title[i]
            data['links'] = links[i]
            JobData.append(data)
      return JobData

if __name__ == '__main__':
      app.run()

