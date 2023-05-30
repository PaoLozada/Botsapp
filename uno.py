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
    element = driver.find_element(By.XPATH,"//h3[contains(.,'Filtrar por capacidad de memoria')]")
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
        print (ref.text)
        print(val.text)
    data['Ktronix']=[referencia, valor]
    print(data)
    # Convertir el diccionario a JSON
    #json_datos = json.dumps(data)

    # Imprimir el JSON
    #print(json_datos)

    return(data)




def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
