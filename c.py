from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
f0 = open("c_GHTB.txt", "w", encoding='utf-8')
try:
    url = "https://nordicmaster.github.io"
    driver.get(url)
    driver.implicitly_wait(12)
    elem = driver.find_element(By.CLASS_NAME, "bodytype")
    driver.get(url + "/about.html")
    driver.back()
    driver.refresh()    
    elem = driver.find_element(By.CLASS_NAME, "bodytype")
    assert elem is not None
    assert elem.size['width'] is not None
    assert elem.size['width'] > 1080
    lst = driver.find_elements(By.CLASS_NAME, "solid")
    sumall = 0    
    for item in lst:
        assert item is not None
        childs = item.find_elements(By.XPATH, "descendant::div[2]")
        for dd in childs:
            assert dd is not None
            dd.find_element(By.XPATH, "descendant::summary").click()
            assert dd.text is not None
            f0.write(dd.find_element(By.CSS_SELECTOR, "p").text);
            f0.write('\n')
        childs = item.find_elements(By.CSS_SELECTOR, "div[class='inlineblock vertical-align marginleft halfwidth smalltext']")
        for dd in childs:
            assert dd is not None
            len = dd.find_element(By.CLASS_NAME, "ng-scope")
            numlen = float(len.text[:len.text.index(' ')])
            sumall += numlen;            
            assert numlen is not None
            assert numlen > 0
            f0.write(str(numlen))
            f0.write('\n')
    f0.write("total: " + str(int(sumall) // 60) + " : " + str(int(sumall) % 60))
    f0.write('\n')
    print('GTHB test success')
finally:
    f0.close()
    driver.quit()