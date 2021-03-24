import time, linecache, selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def headlessDriv():
    """
    Returns a Selenium Chrome connection defaulted to headless mode (no gui).
    \nArgs --> None
    \nReturns --> webdriver.Chrome object
    \nRaises --> None
    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument("-incognito")
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    return (webdriver.Chrome(executable_path=r"C:\Program Files\PATH\chromedriver",chrome_options=None))  # Optional argument, if not specified will search path.

def formatUrl(fileName):
    itemdets = str(linecache.getline(str(fileName),1)).split(",")
    userdets = str(linecache.getline(str(fileName),2)).split(",")
    billdets = str(linecache.getline(str(fileName),3)).split(",")
    return (f"https://www.supremenewyork.com/shop/{ str(itemdets[0]) }/{ str(itemdets[1]) }/").strip(),userdets,billdets




def addCurrToBasket(driver):
    WebDriverWait(driver,4).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"add-remove-buttons\"]/input")))
    driver.find_element_by_xpath("//*[@id=\"add-remove-buttons\"]/input").click()

def fillSupremeAddr(driver,addr):
    WebDriverWait(driver,4).until(EC.presence_of_element_located( (By.XPATH, "//*[@id=\"order_billing_name\"]") )).send_keys(addr[0])
    driver.find_element_by_xpath("//*[@id=\"order_email\"]").send_keys(addr[1])
    driver.find_element_by_xpath("//*[@id=\"order_tel\"]").send_keys(addr[2])
    driver.find_element_by_xpath("//*[@id=\"bo\"]").send_keys(addr[3])
    driver.find_element_by_xpath("//*[@id=\"order_billing_address_3\"]").send_keys(addr[4])
    driver.find_element_by_xpath("//*[@id=\"order_billing_city\"]").send_keys(addr[4])
    driver.find_element_by_xpath("//*[@id=\"order_billing_zip\"]").send_keys(addr[5])

def enterCheckout(driver):
    driver.find_element_by_xpath("//*[@id=\"cart\"]/a[2]").click()

def fillSupremeBill(driver,bill):
    driver.find_element_by_xpath("//*[@id=\"cnb\"]").send_keys(bill[0])
    driver.find_element_by_xpath("//*[@id=\"vval\"]").send_keys(bill[1])
    driver.find_element_by_name("credit_card[month]").find_elements_by_tag_name("option").select_by_visible_text(bill[2])
    driver.find_element_by_name("credit_card[year]").find_elements_by_tag_name("option").select_by_visible_text(bill[3])

def main():
    driver = headlessDriv(); url,addr,bill = formatUrl("details.txt"); driver.get(url)
    print("At Supreme Store"); print(url)
    addCurrToBasket(driver)
    enterCheckout(driver)
    fillSupremeAddr(driver,addr)
    fillSupremeBill(driver,bill)



print("Driver closed.")