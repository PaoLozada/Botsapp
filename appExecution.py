from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from page_katro import *
from page_totto import *
from actions import *

mivariable =''
def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True
    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return myDriver

def getBotSearchOffer(driver: webdriver.Chrome) -> str:
    Actions.set_window_position(driver, 0, 0)
    Actions.set_window_size(driver, 1496, 1024)
    data ={}
    referencia = []
    valor =[]
    Actions.open_url(driver, "https://www.ktronix.com/")
    Actions.wait(5)
    Actions.move_to_element(driver, KatroHome.cel)
    Actions.click_element(driver, KatroHome.celu)  
    Actions.wait(3)
   #Actions.click_element(driver, KatroHome.notifi)  
    Actions.scroll_to(driver,751,631)
    Actions.wait(3) 
    Actions.click_element(driver, KatroCell.order) 
    Actions.click_element(driver, KatroCell.menor)
    Actions.wait(5)  
    valPrice=1
    for i in range(3) :
        print(i)
        valRef=str(i+1)
        ref = Actions.get_text(driver, KatroCell.ref_element(valRef))
        val = Actions.get_text(driver, KatroCell.val_element(str(valPrice)))
        referencia.append(ref)
        valor.append(val)
        valPrice+=2
    data['Ktronix']=[referencia, valor]
    return(data)


def getBotSearchNewProducts(driver: webdriver.Chrome, selectItem, category, itemOption) -> str:
    Actions.set_window_position(driver, 0, 0)
    Actions.set_window_size(driver, 1496, 1024)
    Actions.open_url(driver, "https://co.totto.com/")
    Actions.wait(10)
    Actions.click_element(driver, TottoHome.menu_on)
    Actions.wait(4)
    Actions.click_element(driver, TottoHome.new_collection)
    Actions.wait(5)
    item_select = TottoHome.item_select(selectItem)
    Actions.click_element(driver, item_select)
    filter_category = TottoHome.filter_category(category)
    Actions.click_element(driver, filter_category)
    Actions.wait(5)
    filter_option = TottoHome.filter_option(itemOption)
    Actions.click_element(driver, filter_option)
    Actions.wait(5)
    items = Actions.get_texts(driver, TottoHome.product_info)
    data = {'Totto': items}
    return data

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
