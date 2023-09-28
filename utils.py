# validacao dos dados inseridos no sistema importando as bibliotecas necessarias
# from utils import valida_cpf
from validate_docbr import CPF
from datetime import datetime
import re
import requests

def valida_cpf(cpf_input):
    cpf = CPF()
    
    while True:
        
        cpf_input = re.sub('[-.]', '', cpf_input)
        
        resultado = cpf.validate(cpf_input)
        if resultado:
            cpf_formatado = f"{cpf_input[:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{cpf_input[9:]}"
            return cpf_input
        else: 
            cpf_input = print("CPF invalido. Digite novamente: ")
        
    # CONTINUE, para a execucao atual e pula para a proxima
    # BREAK, parar a execucao do laco de repeticao
    # RETURN, retorna a variavel desejada e para a execucao
    # ALTERACAO DA CONDICAO, alterada a condicao 


def valida_rg(rg_input):
    # validacao no padrao RG 11.111.111.-x
    # padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Z-a-z]$'
    
    while True:
        
        rg_input = re.sub('[-.]', '', rg_input)
        
        rg_input = f'{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'
        
        if re.match(padrao_rg, rg_input):
            return rg_input
        else:
            rg_input = input("RG invalido. Digite novamente: ")

def valida_data_nascimento(data_nascimento_input):
    
        # print(data_nascimento_input)
        # print(type(data_nascimento_input))
        
    while True:
        
        data_nascimento_input = input("Digite a data de nascimento: ")
        try:
            data_convertida = datetime.strptime(data_nascimento_input, '%d/%m/%Y').date()
            data_atual = datetime.now().date()
            
            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            # print(data_convertida)
            # print(type(data_convertida))
            else:
                print("Data invalida. A sua data de nasimento deve ser anterior a data de hoje. ")
            # inverso
            # data_string = data_convertida.strftime("%d/%m/%Y")
            # print(data_string)
            # print(type(data_string))
            # datetime.strftime
        except ValueError as e:
            print("Formato de data invalido. Voce recebeu o erro: ", e, " Tente novamente")    
        

def buscar_cep(cep_input):
    url = f'https://viacep.com.br/ws/{cep_input}/json/'
    
    response = requests.get(url, verify=False)
    
    # print(type(response))
    # print(response) 
    # print(response[all])
    if response.status_code == 200:
        data = response.json()
        
        endereco = {
            "CEP": data['cep'],
            "Logradouro": data['logradouro'],
            "Bairro": data['bairro'],
            "Cidade": data['localidade'],
            "Estado": data['uf'],
        }
        return endereco
    
buscar_cep(81010270)

