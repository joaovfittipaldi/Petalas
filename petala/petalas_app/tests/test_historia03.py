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
        default_page(driver)

        #encontra o botão Doação e clica
        entra_turmas = driver.find_element(By.ID, 'turmas')
        entra_turmas.click()
        time.sleep(1)

        # acessa turma
        ver_turma = driver.find_element(By.ID, 'acessa_turma')
        ver_turma.click()
        time.sleep(1)

        # seleciona a crianca para visualizar
        ver_crianca = driver.find_element(By.ID, 'acessa_crianca')
        ver_crianca.click()
        time.sleep(1)
        



