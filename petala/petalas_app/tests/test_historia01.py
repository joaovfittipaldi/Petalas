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
        nome_crianca = driver.find_element(By.ID, 'inputNome')
        nome_crianca.click()
        nome_crianca.send_keys('Julia Almeida')
        time.sleep(1)

        # insere a idae da crianca 
        idade_crianca = driver.find_element(By.ID, 'inputIdade')
        idade_crianca.click()
        idade_crianca.send_keys("10")
        time.sleep(1)

        # insere a data de nascimento
        data_nascimento = driver.find_element(By.ID, 'inputNascimento')
        data_nascimento.click()
        data_nascimento.send_keys('10112007')
        time.sleep(1)
    

        #insere o periodo da crianca
        selecionar_turno = driver.find_element(By.ID, 'inputPeriodo')
        #padrinho_doacao.click()
        select = Select(selecionar_turno)
        select.select_by_visible_text("Manhã")
        time.sleep(1)

        # insere a data de entrada da crianca na ong
        data_entrada = driver.find_element(By.ID, 'inputCity')
        data_entrada.click()
        data_entrada.send_keys('10032021')
        time.sleep(1)

        # insere o tempo de permanencia da crianca na ong
        tempo_permanencia = driver.find_element(By.ID, 'inputZip')
        tempo_permanencia.click()
        tempo_permanencia.send_keys('2 meses')
        time.sleep(1)

        #insere o periodo da crianca
        selecionar_turma = driver.find_element(By.ID, 'inputTurma')
        #padrinho_doacao.click()
        select = Select(selecionar_turma)
        select.select_by_visible_text("Eu e o Mundo - Tarde")
        time.sleep(1)
        
        #insere a avaliacao da crianca
        selecionar_avaliacao = driver.find_element(By.ID, 'inputAutoavaliacao')
        #padrinho_doacao.click()
        select = Select(selecionar_avaliacao)
        select.select_by_visible_text("Verde")
        time.sleep(1)
        
        # informa o status da crianca
        status_crianca = driver.find_element(By.ID, 'inputStatus')
        status_crianca.click()
        status_crianca.send_keys('Meiga, Gentil e com otimo comportamento!')
        time.sleep(1)

        #aperta o botao cadastro
        botao_cadastrarcrianca = driver.find_element(By.ID, 'botao_cadastrarcrianca')
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
        nome_crianca = driver.find_element(By.ID, 'inputNome')
        nome_crianca.click()
        nome_crianca.send_keys('Emanuel Eduardo')
        time.sleep(1)

        # insere a idae da crianca 
        idade_crianca = driver.find_element(By.ID, 'inputIdade')
        idade_crianca.click()
        idade_crianca.send_keys("11")
        time.sleep(1)

        # insere a data de nascimento
        data_nascimento = driver.find_element(By.ID, 'inputNascimento')
        data_nascimento.click()
        data_nascimento.send_keys('10112008')
        time.sleep(1)
    

        #insere o periodo da crianca
        selecionar_turno = driver.find_element(By.ID, 'inputPeriodo')
        #padrinho_doacao.click()
        select = Select(selecionar_turno)
        select.select_by_visible_text("Manhã")
        time.sleep(1)

        # insere a data de entrada da crianca na ong
        data_entrada = driver.find_element(By.ID, 'inputCity')
        data_entrada.click()
        data_entrada.send_keys('10032021')
        time.sleep(1)

        # insere o tempo de permanencia da crianca na ong
        tempo_permanencia = driver.find_element(By.ID, 'inputZip')
        tempo_permanencia.click()
        tempo_permanencia.send_keys('3 meses')
        time.sleep(1)

        #insere o periodo da crianca
        selecionar_turma = driver.find_element(By.ID, 'inputTurma')
        #padrinho_doacao.click()
        select = Select(selecionar_turma)
        select.select_by_visible_text("Eu e o Mundo - Tarde")
        time.sleep(1)
        
        #insere a avaliacao da crianca
        selecionar_avaliacao = driver.find_element(By.ID, 'inputAutoavaliacao')
        #padrinho_doacao.click()
        select = Select(selecionar_avaliacao)
        select.select_by_visible_text("Verde")
        time.sleep(1)
        
        # informa o status da crianca
        status_crianca = driver.find_element(By.ID, 'inputStatus')
        status_crianca.click()
        status_crianca.send_keys('Meiga, Gentil e com otimo comportamento!')
        time.sleep(1)

        #aperta o botao cadastro
        botao_cadastrarcrianca = driver.find_element(By.ID, 'botao_cadastrarcrianca')
        botao_cadastrarcrianca.click()
        time.sleep(1)