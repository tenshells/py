from selenium import webdriver
from selenium.webdriver.chrome.service import Service

sideurl = 'https://www.google.com/'
mainurl = 'https://www.scaler.com/'
jobsurl = 'academy/mentee-dashboard/careers-hub/applications/'

options = webdriver.ChromeOptions() 
service = Service(executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
options.add_argument("user-data-dir=C:\\Users\\shelt\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
options.add_argument(r'--profile-directory=Default')
# options.add_argument(r'disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
w = webdriver.Chrome(service=service,options=options)
# w = webdriver.Chrome()
w.get(sideurl)

print(w.title)
w.close()
