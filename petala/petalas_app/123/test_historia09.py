from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#REGISTRAR LISTA DE PRESENÇA DIÁRIA DAS CRIANÇAS

class Historia09(LiveServerTestCase):
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
        
        # adiciona lista de presenca 
        add_novo_dia = driver.find_element(By.ID, 'novo_dia')
        add_novo_dia.click()
        time.sleep(1)

        # adiciona lista de presenca 
        abre_chamada = driver.find_element(By.ID, 'inputData')
        abre_chamada.click()
        abre_chamada.send_keys('10112023')
        time.sleep(1)

        seleciona_crianca = driver.find_element(By.ID, 'checkCrianca')
        seleciona_crianca.click()
        
        confirma_crianca = driver.find_element(By.ID, 'cadastro_dia')
        confirma_crianca.click()