from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#ENCONTRAR UMA CRIANÇA PELO NOME (PESQUISAR)

class Historia07(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_007_scenario1(self):

        driver = setup_selenium()

        default_page(driver)

        #CLICA NA BARRA DE PESQUISA
        pesquisar_crianca = driver.find_element(By.ID, 'busca')

        #escreve e acha João
        pesquisar_crianca.send_keys('João')
        time.sleep(1)
        
        pesquisar_crianca.send_keys(Keys.RETURN)
        time.sleep(1)
        
    def test_007_scenario2(self):

        driver = setup_selenium()

        default_page(driver)

        #CLICA NA BARRA DE PESQUISA
        pesquisar_crianca = driver.find_element(By.ID, 'busca')
        
        #escreve Maria e não encontra
        pesquisar_crianca.send_keys('Luisa')
        time.sleep(1)

        pesquisar_crianca.send_keys(Keys.RETURN)
        time.sleep(1)