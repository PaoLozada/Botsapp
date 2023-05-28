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
    driver.set_window_size(1280, 1024)
    print('ingresaaa')
    acciones = ActionChains(driver)
    data ={}
    driver.get("https://www.ktronix.com/")
    das = driver.current_url
    print(das)
    print('unooooooooooooooooooooooooooooooooooooo')
    cel = driver.find_element(By.XPATH,"(//a[@title='Celulares'])[1]")
    acciones.move_to_element(cel).perform()
    celu = driver.find_element(By.XPATH,"//a[@data-subcategory='Celulares']")
    celu.click()
    time.sleep(10)
    print('dosssssssssssssssssssssssssssssssssssssssssssssssss')
    order = driver.find_element(By.XPATH,"//div[contains(@class,'float-select js-float-select js-float-group full-width active-click')]")
    order.click()
    driver.execute_script("window.scrollTo(0, 1100);")
    print('tresssssssssssssssssssssssssssssssssssssssss')
    menor = driver.find_element(By.XPATH,"//li[contains(.,'Precio: menor a mayor')]")
    menor.click()
    time.sleep(10)
    print('cuatroooooooooooooooooooooooooooo')
    caption = driver.find_element(By.XPATH,"//div[@class='algolia-stats'][contains(.,'Mostrando 25 de 335 resultados')]")
    print(caption.text)
    print('cincooooooooooooooooooooo')
    mivariable = caption.text
    
    time.sleep(10)
    referencia = []
    valor =[]

    for i in range(5) :
        print(i)
        valRef=str(i+1)
        #valVal=str((i+1)*2)
        ref = driver.find_element(By.XPATH,"(//div[@class='product__item__information__brand'])["+valRef+"]")
        val = driver.find_element(By.XPATH,"(//span[contains(@class,'price')])["+valRef+"]")
        referencia.append(ref.text)
        valor.append(val.text)
        print (ref.text)
        print(val.text)
    data['Ktronix']=[referencia, valor]
    print(data)
    return(mivariable)




def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
