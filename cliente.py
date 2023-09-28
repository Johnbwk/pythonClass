from utils import valida_cpf, valida_rg, valida_data_nascimento, buscar_cep
from banco_dados import select_banco_dados, insert_banco_dados


def menu_cliente():
    validador_menu = True
    lista_cliente = []
    
    while validador_menu:
        print('''Bem vindoa area do cliente, selecione uma das opções abaixo: 
        1 - Cadastrar Cliente
        2 - Alterar Cliente
        3 - Buscar Cliente
        4 - Deletar Cliente
        5 - Listar Clientes
        6 - Voltar ao menu anterior''')
        opcao = int(input("Digite a opcao desejada do menu cliente: "))
        if opcao == 1:
            cliente_dicionario = {
                "Nome": input("Digite o nome do cliente: "),
                "CPF": valida_cpf(input("Digite o CPF: ")),
                "RG": valida_rg(input("Digite o RG: ")),
                "Nascimento": valida_data_nascimento(input("Digite a data de nascimento")),
                "Endereco": buscar_cep(input("Digite o CEP do cliente: ")),
                "Numero residencia": input("Digite o numero da residencia: ")
            }
            lista_cliente.append(cliente_dicionario)
        elif opcao == 2:
            print("Atualizar cadastro do cliente ")
            cliente = int(input("Digite o CPF do cliente para atualizar: "))
            update_banco_dados(input_cpf)
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            print(lista_cliente)
        elif opcao == 6:
            validador_menu = False
            print("Saindo do programa")
        else:
            print("Favor selecionar uma opçáo válida")

