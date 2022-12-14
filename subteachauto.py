from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(PATH,options=options)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

ACCOUNT = "account@gmail.com"
PASSWORD = "password"

driver.get('https://subteachersource.com/Account/login')
driver.find_element_by_id("Email").send_keys(ACCOUNT)
driver.find_element_by_id("Password").send_keys(PASSWORD)
driver.find_element_by_id("submit").click()

driver.get("https://subteachersource.com/SubLongTermOpenings")

table = driver.find_elements_by_id('SubAssignGrid')

for row in table:
    cells = row.find_elements_by_xpath('//*[@id="SubLongTermAssignGrid"]/div[2]/table/tbody/tr/td')
    if cells[4].text == "*Specific School*":
        button = cells[9].find_element_by_xpath("//*[@id='SubLongTermAssignGrid']/div[2]/table/tbody/tr/td[10]/a")
        button.click()
        
obj = driver.switch_to.alert.
msg=obj.text
print("Alert shows following message: "+ msg )
obj.accept()