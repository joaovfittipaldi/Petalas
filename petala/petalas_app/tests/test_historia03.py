from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#VISUALIZAR INFORMAÇÕES DE UMA CRIANÇA

class Historia03(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_003_scenario1(self):

        driver = setup_selenium()

        #encontra o botão doação e clica
        doacao = driver.find_element(By.ID, 'doacao')
        doacao.click()
        time.sleep(1)

        #registra nova doacao
        ver_doacao = driver.find_element(By.ID, 'nova_doacao')
        ver_doacao.click()
        time.sleep(1)


# Seu array de IDs
ids_array = ["elemento1", "elemento2", "elemento3"]

# Caminho para o driver do navegador (certifique-se de ter o driver instalado)
driver = webdriver.Chrome("caminho/do/seu/chromedriver")

# Itera sobre os IDs no array
for element_id in ids_array:
    # Abre uma página de exemplo (substitua pela sua URL)
    driver.get("https://www.example.com")

    try:
        # Localiza o elemento com base no ID atual
        element = driver.find_element_by_id(element_id)

        # Realiza alguma ação no elemento (exemplo: clicar)
        element.click()

        # Faça mais ações ou asserções conforme necessário
        # ...

    except Exception as e:
        print(f"Erro ao interagir com o elemento {element_id}: {e}")

# Fecha o navegador no final dos testes
driver.quit()
