#Note: This code isn't finished yet 

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver opens edge and then opens dominos pizza, We're using edge here because chrome is having issues with clicking a bloody button lol
driver = webdriver.Edge()
driver.get('https://www.dominos.co.uk')
#-----------------------------------------------
time.sleep(2)

driver.find_element("xpath", "/html/body/div[4]/div[2]/div/div/div[2]/div/div/button").click()


postcode = driver.find_element("xpath","/html/body/div[2]/div/div/div/section/div/section[1]/div/div/div[2]/form/div[2]/div[1]/div[2]/input")
postcode.send_keys("POSTCODE") #<change post code 

time.sleep(2)

driver.find_element("xpath","/html/body/div[2]/div/div/div/section/div/section[1]/div/div/div[3]/button[1]/div").click() #clicks delivery
time.sleep(2)
driver.find_element("xpath", "/html/body/div[2]/div/div/div/main/section/div[5]/section/div[2]/div/section/button[2]/div").click() # clicks deny thingy
time.sleep(2)

driver.find_element("xpath","/html/body/div[2]/div/div/div/main/section/section[1]/section[1]/div[5]/div[1]/picture/img")
time.sleep(1000)



#temp time


