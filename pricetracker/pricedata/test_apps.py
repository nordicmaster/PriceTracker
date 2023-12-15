
from .models import PriceItem
from decimal import Decimal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .models import Preview
from datetime import datetime


def get_price(name):
    driver = webdriver.Firefox()
    result_string = []
    try:
        driver.get(f'https://www.ozon.ru/search/?text={name.replace(" ","+")}&from_global=true')

        wait = WebDriverWait(driver, 60)
        find_price = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'i5o')))

        result_string.append(driver.title)
        items = driver.find_elements(By.CLASS_NAME, "i5o")
        # result_string.append(driver.page_source)
        result_string.append(len(items))
        for el in items:
            pict = el.find_element(By.CLASS_NAME, "c9-a").get_attribute("src")
            el1 = el.find_element(By.CLASS_NAME, "i6o")
            price_text = el1.find_element(By.CLASS_NAME, "d6-a0").text
            caption_text = el1.find_element(By.CLASS_NAME, "vd7").text
            result_string.append(f'{caption_text} - {price_text} - {pict}')
            price_decimal = Decimal(price_text.split(' ', 1)[0].split("\u2009", 1)[0])
            preview_item = Preview(image_url=pict)
            pitem = PriceItem(name=caption_text, date=datetime.now(), price=price_decimal, preview=preview_item)
            preview_item.save()
            pitem.save()
    finally:
        driver.quit()
    return result_string


# def push_item(item: PriceItem):
#    item.save()
#    return


def get_all_items():
    # return PriceItem.objects.order_by("-date").distinct("name")
    return PriceItem.objects.all()
