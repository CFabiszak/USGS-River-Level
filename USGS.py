from selenium import webdriver
path=r'C:\Users\codyf\Desktop\driver\chromedriver' #change the path to where you have chromedriver saved
import time
from selenium.webdriver.common.keys import Keys

option= webdriver.ChromeOptions()
option.add_argument('--incognito')

driver=webdriver.Chrome(path,chrome_options=option)
driver.get("https://waterdata.usgs.gov/usa/nwis/uv?01636500")

search= driver.find_element_by_xpath("""//*[@id="html"]""").click()
search_day=driver.find_element_by_xpath("""//*[@id="begin_date"]""").click()
search_day_clear=driver.find_element_by_xpath("""//*[@id="begin_date"]""").clear()
date=search_day_clear=driver.find_element_by_xpath("""//*[@id="begin_date"]""")
date.send_keys((time.strftime("%Y-%m-%d")))
date.send_keys(Keys.RETURN)
date.send_keys(Keys.RETURN)
post = driver.find_elements_by_xpath("""/html/body/table[1]/tbody""")

for posts in post:
    print(posts.text )
driver.quit()
