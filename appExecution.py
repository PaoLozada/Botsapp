from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json

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
    driver.set_window_position(0, 0)
    driver.set_window_size(1496, 1024)
    acciones = ActionChains(driver)
    data ={}
    driver.get("https://www.ktronix.com/")
    cel = driver.find_element(By.XPATH,"(//a[@title='Celulares'])[1]")
    acciones.move_to_element(cel).perform()
    celu = driver.find_element(By.XPATH,"//a[@data-subcategory='Celulares']")
    celu.click()
    time.sleep(2)
    notifi = driver.find_element(By.XPATH,"//button[@class='button-primary js-cookie-notification-accept']")
    notifi.click()
    driver.execute_script("window.scrollTo(751, 631);")
    time.sleep(2)
    order = driver.find_element(By.XPATH,"//div[@class='float-select js-float-select js-float-group full-width active-click']")
    order.click()
    menor = driver.find_element(By.XPATH,"//li[contains(.,'Precio: menor a mayor')]")
    menor.click()
    time.sleep(5)
    referencia = []
    valor =[]

    for i in range(3) :
        print(i)
        valRef=str(i+1)
        ref = driver.find_element(By.XPATH,"(//div[@class='product__item__information__brand'])["+valRef+"]")
        val = driver.find_element(By.XPATH,"(//span[contains(@class,'price')])["+valRef+"]")
        referencia.append(ref.text)
        valor.append(val.text)
    data['Ktronix']=[referencia, valor]
    print(data)
    return(data)


def getBotSearchNewProducts(driver: webdriver.Chrome,  category,  itemOption) -> str:
    driver.set_window_position(0, 0)
    driver.set_window_size(1496, 1024)
    driver.get("https://co.totto.com/")
    # Esperar a que la página cargue completamente
    driver.implicitly_wait(10)
    menu=driver.find_element(By.ID,'menu_on')
    menu.click()
    newCollection=driver.find_element(By.XPATH,"//a[contains(.,'Nueva colección')]")
    newCollection.click()
    time.sleep(5)
    selector = "2"
    itemSelect= driver.find_element(By.XPATH,"(//img[@class=' b-error'])["+selector+"]")
    itemSelect.click()
    filter = category
    fil = driver.find_element(By.XPATH,"(//h5[contains(.,'"+filter+"')])[2]")
    fil.click()
    filterSelect=itemOption
    color = driver.find_element(By.XPATH,"//a[@title='"+filterSelect+"']")
    color.click()
    items=[]
    data ={}
    time.sleep(5)
    ref= driver.find_elements(By.XPATH,"//div[@class='_product-info']/h3/span[1]")
    for i in ref:
        print (i.text)
        items.append(i.text)
    data['Totto']=items
    return(data)

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
