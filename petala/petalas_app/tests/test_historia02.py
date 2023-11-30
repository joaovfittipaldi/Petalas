from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#VISUALIZAR A LISTA DE CRIANÇAS NA TURMA

class Historia02(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_002_scenario1(self):

        driver = setup_selenium()
        default_page(driver)

        #encontra o botão turmas e clica
        buscar_nome = driver.find_element(By.ID, 'turmas')
        buscar_nome.click()
        time.sleep(1)

        #turma eu e o mundo - manhã
        buscar_nome = driver.find_element(By.ID, 'acessa_turma')
        buscar_nome.click()
        time.sleep(1)
    