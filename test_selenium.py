from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
prefs = {
'profile.default_content_setting_values' :
{
'notifications' : 2
}
}
options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(chrome_options = options)
driver.maximize_window()
driver.get("https://www.t1.dreame.com/")
driver.implicitly_wait(5)



driver.find_element_by_xpath('/html/body/div/div[1]/div/button[1]').click()

driver.find_elements_by_class_name("Column_column-item__M8mPX")[1].click()


driver.find_element_by_class_name('rc-input').send_keys('luna')

driver.find_element_by_class_name('rc-input-prefix').click()

driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/div[1]/a/div/div/div/img').click()

driver.switch_to.window(driver.window_handles[1])


driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[6]/button').click()

ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div/ul/li[1]')).perform()

driver.implicitly_wait(5)

driver.find_elements_by_css_selector('.ChapterListDesktop_chapter-list-item__mcfys .dreame-font')[1].click()



driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[1]/div[3]/button').click()
#
#all_buy_button=driver.find_element(By.CSS_SELECTOR, ".dm-button:nth-child(1) > span")


# all_buy_button=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/button')
#
#
# print(all_buy_button)

try:

 driver.implicitly_wait(2)

 all_buy_button=driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/button")

 driver.implicitly_wait(3)
 print(all_buy_button)

 if all_buy_button:
  all_buy_button.click()

except Exception as e:
 print(e)


driver.switch_to.window(driver.window_handles[2])

driver.implicitly_wait(10)


# ActionChains.move_to_element(driver.find_element_by_id('agree-service')).perform()
#
# WebDriverWait(driver, 5).until(
#  EC.presence_of_element_located((By.ID, 'agree-service'))
#  ).send_keys(Keys.SPACE)

# driver.find_element_by_id('agree-service').click()
driver.find_element(By.CSS_SELECTOR, "label").click()

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[4]/div[3]').click()

driver.find_element_by_xpath('/html/body/div/div/section/section/ul/li[1]/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div/div/section/section/ul/li[1]/div[1]/input').send_keys('594568079@qq.com')
driver.find_element_by_xpath('/html/body/div/div/section/section/ul/li[2]/div[1]/input').click()
driver.find_element_by_xpath('/html/body/div/div/section/section/ul/li[2]/div[1]/input').send_keys('123456')


WebDriverWait(driver, 5).until(
 EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/section/section/button'))
 ).click()

time.sleep(10)






#WebDriverWait(driver,5).until(EC.text_to_be_present_in_element_value((By.XPATH,'/html/body/div/div[4]/main/div/section/section[1]/div/section/a/span'),'MORE'))


driver.quit()

