from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium_setup import *

import time

#CADASTRAR UMA CRIANÇA

class Historia01(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        setup_selenium()

    @classmethod
    def tearDownClass(cls):
        finalizar_selenium()

    def test_001_scenario1(self):

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

        #clica para criar nova crianca
        caastrar_novacrianca = driver.find_element(By.ID, 'registrar_crianca')
        caastrar_novacrianca.click()
        time.sleep(1)

        # insere o nome da crianca
        nome = driver.find_element(By.ID, 'nome')
        nome.click()
        nome.send_keys('Maria Joaquina')
        time.sleep(1)

        # insere a idae da crianca 
        idade = driver.find_element(By.ID, 'idade')
        idade.click()
        idade.send_keys("10")
        time.sleep(1)

        # insere a data de nascimento
        data_nascimento = driver.find_element(By.ID, 'nascimento')
        data_nascimento.click()
        data_nascimento.send_keys('10112007')
        time.sleep(1)
    

        # insere a data de entrada da crianca na ong
        data_entrada = driver.find_element(By.ID, 'data_entrada')
        data_entrada.click()
        data_entrada.send_keys('10032021')
        time.sleep(1)

        cpf_crianca = driver.find_element(By.ID, 'cpf_crianca')
        cpf_crianca.click()
        cpf_crianca.send_keys('89745387921')
        time.sleep(1)

        nome_responsavel = driver.find_element(By.ID, 'nome_responsavel')
        nome_responsavel.click()
        nome_responsavel.send_keys('Júlia Ferraz')
        time.sleep(1)

        cpf_responsavel = driver.find_element(By.ID, 'cpf_responsavel')
        cpf_responsavel.click()
        cpf_responsavel.send_keys('989765433911')
        time.sleep(1)

        email_responsavel = driver.find_element(By.ID, 'email_responsavel')
        email_responsavel.click()
        email_responsavel.send_keys('juliaff@cesar.school')
        time.sleep(1)

        telefone_responsavel = driver.find_element(By.ID, 'telefone_responsavel')
        telefone_responsavel.click()
        telefone_responsavel.send_keys('81999767867')
        time.sleep(1)

        #aperta o botao cadastro
        botao_cadastrarcrianca = driver.find_element(By.ID, 'botao_cadastrar_crianca')
        botao_cadastrarcrianca.click()
        time.sleep(1)

    def test_001_scenario2(self):

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

        #clica para criar nova crianca
        caastrar_novacrianca = driver.find_element(By.ID, 'registrar_crianca')
        caastrar_novacrianca.click()
        time.sleep(1)

        # insere o nome da crianca
        nome_crianca = driver.find_element(By.ID, 'nome')
        nome_crianca.click()
        nome_crianca.send_keys('Lucas Carlos')
        time.sleep(1)

        # insere a idae da crianca 
        idade_crianca = driver.find_element(By.ID, 'idade')
        idade_crianca.click()
        idade_crianca.send_keys("11")
        time.sleep(1)

        # insere a data de nascimento
        data_nascimento = driver.find_element(By.ID, 'nascimento')
        data_nascimento.click()
        data_nascimento.send_keys('10112008')
        time.sleep(1)

        # insere a data de entrada da crianca na ong
        data_entrada = driver.find_element(By.ID, 'data_entrada')
        data_entrada.click()
        data_entrada.send_keys('10032021')
        time.sleep(1)

        cpf_crianca = driver.find_element(By.ID, 'cpf_crianca')
        cpf_crianca.click()
        cpf_crianca.send_keys('09876545632')
        time.sleep(1)

        nome_responsavel = driver.find_element(By.ID, 'nome_responsavel')
        nome_responsavel.click()
        nome_responsavel.send_keys('Marcos Gabriel')
        time.sleep(1)

        cpf_responsavel = driver.find_element(By.ID, 'cpf_responsavel')
        cpf_responsavel.click()
        cpf_responsavel.send_keys('00978656711')
        time.sleep(1)

        email_responsavel = driver.find_element(By.ID, 'email_responsavel')
        email_responsavel.click()
        email_responsavel.send_keys('mga@cesar.school')
        time.sleep(1)

    
        telefone_responsavel = driver.find_element(By.ID, 'telefone_responsavel')
        telefone_responsavel.click()
        telefone_responsavel.send_keys('119876539239')
        time.sleep(1)

        #aperta o botao cadastro
        botao_cadastrarcrianca = driver.find_element(By.ID, 'botao_cadastrar_crianca')
        botao_cadastrarcrianca.click()
        time.sleep(1)