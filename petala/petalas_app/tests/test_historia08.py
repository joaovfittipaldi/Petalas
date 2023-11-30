from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#PESQUISAR DOADOR

class Historia08(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_008_scenario1(self):

        driver = setup_selenium()

        default_page(driver)

        #CLICA NA BARRA DE PESQUISA
        pesquisar_crianca = driver.find_element(By.ID, 'busca')

        #escreve e acha Cleber
        pesquisar_crianca.send_keys('Cleber')
        time.sleep(1)
        
        pesquisar_crianca.send_keys(Keys.RETURN)
        time.sleep(1)

    def test_008_scenario2(self):

        driver = setup_selenium()

        default_page(driver)

        #CLICA NA BARRA DE PESQUISA
        pesquisar_crianca = driver.find_element(By.ID, 'busca')

        #escreve e não encontra Marcos
        pesquisar_crianca.send_keys('Marcos')
        time.sleep(1)

        pesquisar_crianca.send_keys(Keys.RETURN)
        time.sleep(1)    