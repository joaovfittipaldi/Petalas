from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#HISTORIA DE CADASTRO DE DOAÇÃO

class Historia04(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_004_scenario1(self):

        driver = setup_selenium()

        default_page(driver)

        #encontra o botão doação e clica
        doacao = driver.find_element(By.ID, 'doacao')
        doacao.click()
        time.sleep(1)

        #registra nova doacao
        nova_doacao = driver.find_element(By.ID, 'nova_doacao')
        nova_doacao.click()
        time.sleep(1)
        
        # insere o nome do padrinho 
        padrinho_doacao = driver.find_element(By.ID, 'inputNomePadrinho')
        padrinho_doacao.click()
        padrinho_doacao.send_keys('Marcos Pedro')
        time.sleep(1)

        # insere o cpf do padrinho 
        cpf_doacao = driver.find_element(By.ID, 'inputCPF')
        cpf_doacao.click()
        cpf_doacao.send_keys('780285589290')
        time.sleep(1)

        # insere o valor da doação   
        valor_doacao = driver.find_element(By.ID, 'inputValor')
        valor_doacao.click()
        valor_doacao.send_keys("200")
        time.sleep(1)
        
        # insere o nome da criança
        crianca_doacao = driver.find_element(By.ID, 'inputNomeCrianca')
        crianca_doacao.click()
        crianca_doacao.send_keys('Matheus Henrique')
        time.sleep(1)
    
        # insere a descricao da doacao 
        descricao_doacao = driver.find_element(By.ID, 'inputDescricao')
        descricao_doacao.click()
        descricao_doacao.send_keys('Se cuida, você é um menino bom!')
        time.sleep(1)
        

        #aperta o botao cadastro
        botao_cadastrar = driver.find_element(By.ID, 'botao_cadastrar')
        botao_cadastrar.click()
        time.sleep(1)
    
    def test_004_scenario2(self):

        driver = setup_selenium()

        default_page(driver)

        #encontra o botão doação e clica
        doacao = driver.find_element(By.ID, 'doacao')
        doacao.click()
        time.sleep(1)

        #registra nova doacao
        nova_doacao = driver.find_element(By.ID, 'nova_doacao')
        nova_doacao.click()
        time.sleep(1)
        
        # insere o nome do padrinho 
        padrinho_doacao = driver.find_element(By.ID, 'inputNomePadrinho')
        padrinho_doacao.click()
        padrinho_doacao.send_keys('João Marcelo')
        time.sleep(1)

        # insere o cpf do padrinho 
        cpf_doacao = driver.find_element(By.ID, 'inputCPF')
        cpf_doacao.click()
        cpf_doacao.send_keys('56489734298')
        time.sleep(1)

        # insere o valor da doação   
        valor_doacao = driver.find_element(By.ID, 'inputValor')
        valor_doacao.click()
        valor_doacao.send_keys("125")
        time.sleep(1)
        
        # insere o nome da criança
        crianca_doacao = driver.find_element(By.ID, 'inputNomeCrianca')
        crianca_doacao.click()
        crianca_doacao.send_keys('Márcio Felipe')
        time.sleep(1)
    
        # insere a descricao da doacao 
        descricao_doacao = driver.find_element(By.ID, 'inputDescricao')
        descricao_doacao.click()
        descricao_doacao.send_keys('Você é muito inteligente, se cuida!')
        time.sleep(1)
        

        #aperta o botao cadastro
        botao_cadastrar = driver.find_element(By.ID, 'botao_cadastrar')
        botao_cadastrar.click()
        time.sleep(1)
        