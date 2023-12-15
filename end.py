from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def pxp_end():
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    f0 = open("end_log.txt", "w", encoding='utf-8')
    try:
        url = "http://webtool"
        driver.get(url)
        driver.implicitly_wait(5)
        #alert0 = driver.switch_to.alert
        #if alert0 is not None:
        #    alert0.send_keys("ryabukhinda")
        #    alert0.send_keys(Keys.TAB)
        #    alert0.send_keys("mmtr_43")
        #    alert0.accept()
        elem = driver.find_element_by_xpath("//button[contains(text(), 'Завершить')]")
        assert elem is not None
        f0.write("found at " + str(time.ctime()));
        f0.write('\n')
        time.sleep(50*60)
        #time.sleep(3)
        elem.click()
        f0.write("clicked at " + str(time.ctime()));
        f0.write('\n')
        print('pxp_end test success')
    finally:
        f0.close()
        driver.quit()
        
def btrx_end():
    driver = webdriver.Chrome()
    f0 = open("end_log.txt", "w", encoding='utf-8')
    try:
        url = "https://phimproject.bitrix24.ru/";
        driver.get(url)
        driver.implicitly_wait(5)
        
        driver.find_element_by_xpath("//input[@id='login']").send_keys("ryabukhinda@phimproject.ru")
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(), 'Далее')]").click()
        time.sleep(10)

        driver.find_element_by_xpath("//input[@id='password']").send_keys("qwe1234567890")
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(), 'Далее')]").click()
        time.sleep(10)

        elem = driver.find_element_by_xpath("//span[contains(text(), 'Работаю')]")
        f0.write("found at " + str(time.ctime()))
        f0.write('\n')
        elem.click()
        time.sleep(1)
        elem2 = driver.find_element_by_xpath("//button[contains(text(), 'Завершить рабочий день')]")
        elem2.click()          
        f0.write("btrx clicked at " + str(time.ctime()))
        f0.write('\n')
        time.sleep(10)
        elem3 = driver.find_element_by_xpath("//button[contains(text(), 'Продолжить рабочий день')]")
        assert elem3 is not None
        print('btrx_end test success')
    finally:
        f0.close()
        driver.quit()
        
pxp_end()
btrx_end()