# request = "https://www.scaler.com/users/sign_in/"
# User-Agent:
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

authenticity_token = '9sEUSIorxXVrlzCrJ+RnffndoPFPzXrM5kYNAmArWCB8VPrPuguBeQPRhmKSA9VJLWNKkbuqgrXcK1bzt9g9Fg=='

utf8 = '✓'
# user[email]: shelton.dany@gmail.com
# user[password]: Learn22FutureCPA
# user[remember_me]: 1
# retry: true
grecaptcharesponse='03AFcWeA5E9w1lUMg6KKp0COb9PQrwINB1GRcRJ2J_ie8zUwxbWxSfBEwyrUKaiGLIy0wxJ2VrC8rL2Yi9m6qR_4Oe48EnGdehGLKpg0kOMdIHqmMp5vozbGLljXBSeNtH6Hzh6K6bljOj90ebV7jZzKIw3q8Zo7B4i_bPwxnSotyZKRBSOmhDBYd9T9AveKVCxTgsYAXyVS-cQB8mZ45nldPIwhL3GAPKawoIqT1zUmkP0M9YM3r0kahLKeiO-GdHtXw84d7XG78O_gXpwkrrgLLeKBMo-ApcHSifXWnXDNRYMra2grNLJSX_zwbsvWPvFKWokquwPHQoDcB2IfS8rq5fbWglpCPvD_iyeQRrugFvpTovSmwuxrGmg7z8gykLnLGJT2EMpXcSGmaTAIIJvDRChCuocIMHHiQMBf-yMeNJRaoFvdbPnVnotFFpviptYBWMc8Ur9mBQc-jJ7YoGniBQz6z32afgpn-RUQhRtRDkgtLcnHfWjHw18ibU4NLC04ymbueZu4QRxg_2y13aGFzDLcr8Gx3EPR75QKZCIAH7I6ku1kB1amUAL8iYtyoAOr7gkvdO2Av9'
# commit: Login and Continue

from bs4 import BeautifulSoup as bs
import requests
URL = 'https://www.scaler.com/'
LOGIN_ROUTE = 'users/sign_in/'
HEADERS = {'User-Agent': 'Chrome/79.0.3945.88', 'origin': URL, 'referer': URL + LOGIN_ROUTE}

session = requests.session()

# for i in session.get(URL+LOGIN_ROUTE).cookies:
#     print(i)

login_payload = {
        'email': 'shelton.dany@gmail.com',
        'password': 'Learn22FutureCPA',
        'utf8': utf8,
        'origin': URL, 
        'referer': URL + LOGIN_ROUTE
        }
login_req = session.post(URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
print(login_req.status_code)


JOBURL = 'academy/mentee-dashboard/careers-hub/eligible/'
soup = bs(session.get(URL + JOBURL).text, 'html.parser')

jobs = []

exister = False

for row in soup.select('div.eligible-jobs-list__list'):
    print("exists the div.eligible-jobs-list__list")
    exister=True
    job = row.find('div', class_='presentation')
    jobs.append(job)

if(exister):
    print("got in!")
else:
    print("not in yet")

# print(soup.prettify())

# fi = open('sitehelper.html','w')
# for i in soup.prettify():
#     if(i.isalpha() or i.isascii()):
#         fi.write(i)
# fi.close()