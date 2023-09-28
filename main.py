# Projeto de Python
from cliente import menu_cliente

def exibir_menu():
    validador_menu = True
    # while validador_menu == True:
    while validador_menu:
        print('''Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da ExxonMobil. Selecione uma das opções abaixo para começar: 
        1 - Cliente
        2 - Ordem
        3 - Realizar análise da carteira
        4 - Imprimir relatório da carteira
        5 - Sair''')

        opcao = int(input("Digite a opçao desejada: "))
        if opcao == 1:
            menu_cliente()
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            validador_menu = False
            print("Saindo do programa")
        else:
            print("Favor selecionar uma opçáo válida")

exibir_menu()

#if opcao == 6:
#    print(acao)
#else:
#    print("Favor selecionar uma opção valida")


#Menu Cliente
#1 - Cadastrar Cliente
#2 - Alterar Cliente
#3 - Buscar Cliente
#4 - Deletar Cliente
#5 - Listar Clientes
#6 - Voltar ao menu anterior

#Cadastro menu_cliente
# Nome, CPF, RG, Data de Nascimento, CEP, Número residência.
