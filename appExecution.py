from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unidecode import unidecode
from selenium.webdriver.chrome.options import Options
from page_katro import *
from page_totto import *
from page_comput import *
from page_youtube import *
from actions import *


import time

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def createDriver():
    for i in range(2):
        try:
            return _createDriver()
        except Exception as e:
            print(f"Intento {i+1} falló:", e)
            time.sleep(2)
    raise Exception("No se pudo iniciar Chrome")

def _createDriver():
    chrome_options = Options()
    
    chrome_options.add_argument("--headless=new")
    # Principales
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    chrome_options.add_argument("user-agent=Chrome/120.0.0.0")
    
    prefs = {
        "profile.managed_default_content_settings.images": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)

    return webdriver.Chrome(options=chrome_options)
  
def getBotSearchOffer(driver: webdriver.Chrome) -> str:
    Actions.set_window_position(driver, 0, 0)
    Actions.set_window_size(driver, 1496, 1024)
    data ={}
    referencia = []
    valor =[]
    Actions.open_url(driver, "https://www.ktronix.com/")
    Actions.wait(5)
    Actions.move_to_element(driver, KatroHome.cel)
    Actions.wait(5)
    Actions.click_element(driver, KatroHome.celu)  
    Actions.wait(3)  
    Actions.if_click_element(driver, KatroHome.notifi) 
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
    Actions.if_click_element(driver, TottoHome.close_adv) 
    Actions.click_element(driver, TottoHome.menu_on)
    Actions.wait(4)
    item_select = TottoHome.item_select(selectItem)
    Actions.click_element(driver, item_select)
    Actions.wait(5) 
    Actions.if_click_element(driver, TottoHome.close_adv)       
    filter_category = TottoHome.filter_category(category)
    Actions.click_element(driver, filter_category)
    Actions.wait(5)
    filter_option = TottoHome.filter_option(itemOption)
    Actions.click_element(driver, filter_option)
    Actions.wait(5)
    items = Actions.get_texts(driver, TottoHome.product_info)
    data = {'Totto': items}
    return data

def getBotSearchJob(driver: webdriver.Chrome,city,filter_date,filter_job) -> str:
    Actions.set_window_position(driver, 0, 0)
    Actions.set_window_size(driver, 1496, 1024)
    data ={}
    Actions.open_url(driver,"https://co.computrabajo.com/")
    Actions.wait(10)   
    Actions.send_k(driver,CompuHome.location_input,city)
    Actions.wait(2)
    Actions.click_element(driver, CompuHome.select_position)
    Actions.click_element(driver, CompuVacancies.alert_button)
    Actions.send_k(driver,CompuHome.position_input,filter_job)
    Actions.wait(2)
    Actions.click_element(driver, CompuHome.select_position)
    Actions.click_element(driver, CompuHome.search_button)
    Actions.click_element(driver, CompuVacancies.option_date)
    Actions.click_element(driver, CompuVacancies.filt_date(filter_date))
    jobs_cap = Actions.get_texts(driver, CompuVacancies.jobs)
    places_cap = Actions.get_texts(driver, CompuVacancies.places)
    how_cap= Actions.get_texts(driver, CompuVacancies.how_Long)
    data ["Computrabajo"]= [jobs_cap,places_cap,how_cap]
    return(data)



def getBotSearchViews(driver: webdriver.Chrome, video_name) -> str:
    data = {}
    wait = WebDriverWait(driver, 15)

    search_query = unidecode(video_name).lower()

    driver.get("https://www.youtube.com/")

    # Manejar popup robusto
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button")))
        for btn in buttons:
            if "acept" in btn.text.lower() or "agree" in btn.text.lower():
                btn.click()
                break
    except:
        pass

    
    search_box = wait.until(EC.presence_of_element_located(YtbHome.search_box))
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    
    videos = wait.until(EC.presence_of_all_elements_located(YtbHome.name_video))

    current = False

    for video in videos:
        title = unidecode(video.text).lower()

        try:
            url = video.get_attribute("href")
            if "/shorts/" in url:
                continue
        except:
            continue

        if search_query in title:
            video.click()
            current = True
            break

    if not current:
        data['Youtube'] = ['NO EXISTE']
        return data

   
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

    
    for i in range(2):
        try:
            views = wait.until(EC.presence_of_element_located(YtbVideo.views)).text
            data['Youtube'] = [views]
            return data
        except:
            time.sleep(2)

    data['Youtube'] = ['NO EXISTE']
    return data



def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
