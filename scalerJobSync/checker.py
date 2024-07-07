import requests
from bs4 import BeautifulSoup

url = "https://www.scaler.com/academy/mentee-dashboard/careers-hub/eligible/"
response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')

# print(soup.prettify())

file = open("site.html","w")
for i in soup.prettify():
    if(i.islower() or i.isupper() or i in "<>/#. " or i=='\n'):
        file.write(i)
file.close()

jobs = []

for row in soup.select('div.eligible-jobs-list__list'):
    print("exists the div.eligible-jobs-list__list")
    job = row.find('div', class_='presentation')
    jobs.append(job)

print(jobs)