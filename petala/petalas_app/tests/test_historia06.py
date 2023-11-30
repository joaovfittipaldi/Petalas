from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#VISUALIZAR INFORMAÇÕES DE UMA DOAÇÃO ESPECÍFICA

class Historia06(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_006_scenario1(self):

        driver = setup_selenium()
        default_page(driver)

        #Clica no botão de doações
        #Visualiza as doações pelo nome dos padrinhos
        doacao = driver.find_element(By.ID, 'doacao')
        doacao.click()
        time.sleep(1)
        
        #seleciona padrinho para visualizar doação
        seleciona_doador = driver.find_element(By.ID, 'info_doacao')
        seleciona_doador.click()
        time.sleep(1)


