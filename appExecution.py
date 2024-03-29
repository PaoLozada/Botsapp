from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from unidecode import unidecode
from page_katro import *
from page_totto import *
from page_comput import *
from page_youtube import *
from actions import *


def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")    
    chrome_options.add_argument("user-agent=Chrome/100.0.1000.0")
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True
    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(options=chrome_options)
    #myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
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
    Actions.set_window_position(driver, 0, 0)
    Actions.set_window_size(driver, 1496, 1024)
    data = {}
    current=False
    search_query = unidecode(video_name).lower()
    Actions.open_url(driver, "https://www.youtube.com/")
    Actions.wait(5)
    Actions.send_k(driver, YtbHome.search_box, search_query)
    Actions.return_k(driver, YtbHome.search_box)
    Actions.wait(5)
    videos_current = Actions.get_elements(driver, YtbHome.name_video)
    for i in videos_current:
        current_name= unidecode(i.text).lower()
        if search_query in current_name:
            current=True
            i.click()
            break
    Actions.wait(5)
    video_views = Actions.get_text(driver, YtbVideo.views) if current else 'NO EXISTE'
    print(video_views)
    data['Youtube'] = [video_views]
    return data



def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
