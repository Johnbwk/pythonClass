from cliente import *
from utils import *
import pyodbc


def retornar_cursor_bd():
    connection = pyodbc.connect(retorna_string_conexao_db())
    cursor = connection.cursor()
    return cursor, connection
    

# conexao simples ao banco de dados
def retorna_string_conexao_db():
    return(
        "DRIVER={SQL Server};"
        "SERVER=HOESQL633.NA.XOM.COM;"
        "DATABASE=SkillUp_JBOLWER;"
        # "UID=jbolwer;"
        # "PWD=;"
        "Trusted_connection=yes;"
    )

def select_banco_dados():
   cursor, connection = retornar_cursor_bd()
   cursor.execute("select * from cliente_python;")
   clientes = cursor.fetchall()
   print(clientes)
   connection.commit()

def insert_banco_dados(cliente):
    cursor, connection = retornar_cursor_bd()
    insert_query = """
    INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, numero_residencia);
    VALUES (?, ?, ?, ?, ?, ?);
    """
    
    values = {cliente['nome'], cliente['cpf'], cliente['rg'], cliente['data_nascimento'], cliente['cep']['cep'], cliente['numero_residencia']}
    cursor.execute(insert_query, values)
    connection.commit()

def delete_banco_dados(cpf):
    cursor, connection = retornar_cursor_bd()
    delete_query = "DELETE FROM cliente WHERE cpf = '" + cpf + "';"
    cursor.execute(delete_query)
    connection.commit()

def update_banco_dados(input_cpf):
    cursor, connection = retornar_cursor_bd()
    update_query = """
    UPDATE cliente 
    SET nome = ?, cpf = ?, rg = ?, data_nascimento = ?, cep = ?, numero_residencia = ?;
    WHERE cpf = """ + cliente['CPF'] + """;
    """
    
    set = {cliente['nome'], cliente['cpf'], cliente['rg'], cliente['data_nascimento'], cliente['cep'], cliente['numero_residencia']}
    cursor.execute(update_query, set)
    connection.commit()

cliente = {"nome": "Julio", "cpf": 789456123, "rg": 82415700, "data_nascimento": "28/03/1986", "cep": 81010270, "numero_residencia": 1150 }

insert_banco_dados(cliente)
# insert_banco_dados()
# select_banco_dados()
# delete_banco_dados(cliente["CPF"])
# acesso_banco()
# update_banco_dados(cliente)