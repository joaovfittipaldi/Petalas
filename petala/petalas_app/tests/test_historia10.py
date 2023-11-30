from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#VISUALIZAR CRIANÇAS DA TURMA EM UM DIA

class Historia1o(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_010_scenario1(self):

        driver = setup_selenium()

        default_page(driver)
        
        #encontra o botão turma e entra
        entra_turmas = driver.find_element(By.ID, 'turmas')
        entra_turmas.click()
        time.sleep(1)

        # acessa turma
        ver_turma = driver.find_element(By.ID, 'acessa_turma')
        ver_turma.click()
        time.sleep(1)

        # ver a lista de presença da turma
        ver_lista = driver.find_element(By.ID, 'lista_presenca')
        ver_lista.click()
        time.sleep(1)

        # ver a presenca do aluno
        ver_presenca = driver.find_element(By.ID, 'ver_presenca')
        ver_presenca.click()
        time.sleep(1)