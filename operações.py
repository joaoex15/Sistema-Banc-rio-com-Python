
from bancodedados import*

def deposito(conta,lista) :
    print(f"Saldo Atual da conta R${conta}")
    Valor_int=float(input("Qual valor do depositor R$:"))
    conta=conta+Valor_int
    lista.append(Valor_int)
    return conta


def saque(conta,lista,saques):
    
    print(f"Saldo Atual da conta R${conta}")
    print(f"Só 3 saques diarios,saques já realizados {saques}")
    Valor_int=float(input("Qual valor do saque R$:"))
    if Valor_int > conta:
        print("Valor do saque é maior do que o saldo")
        saque(conta, lista)
    elif Valor_int > 500:
        print("Ultrapassou o limite de saque")
        saque(conta, lista)
    else:
        conta -= Valor_int 
        lista.append(-Valor_int)
        return conta
def extrato(lista):
    print("Segue o extrato da conta")
    for item in lista:
        if item < 0:
            print(f"Saque:R$\033[91m{item}\033[0m")
        else:
            print(f"Extrato:R$+\033[92m{item}\033[0m")




def Add_Client():
    Name=input("Nome do cliente:")
    Data_Nasc=input("Data de nascimento:")
    Cpf=input("Qual é seu cpf:")
    print("Qual seu enderenço completo: ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número da casa: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite a sigla do estado: ")





    lista_name.append(Name)
    Banco_de_dados["nomes"].append([Name])
    Banco_de_dados["Data_nasc"].append(Data_Nasc)
    Banco_de_dados["cpf"].append(Cpf)
    Banco_de_dados["endereço"]["Logradouro"].append(logradouro) 
    Banco_de_dados["endereço"]["Nro"].append(numero) 
    Banco_de_dados["endereço"]["bairro"].append(bairro) 
    Banco_de_dados["endereço"]["cidade"].append(cidade)
    Banco_de_dados["endereço"]["Sigla/estado"].append(estado) 


    for i in range(len(Banco_de_dados["nomes"])):
        print("Nome:", Banco_de_dados["nomes"][i])
        print("Data de Nascimento:", Banco_de_dados["Data_nasc"][i])
        print("CPF:", Banco_de_dados["cpf"][i])
        print("Endereço:")
        print("  Logradouro:", Banco_de_dados["endereço"]["Logradouro"][i])
        print("  Número:", Banco_de_dados["endereço"]["Nro"][i])
        print("  Bairro:", Banco_de_dados["endereço"]["bairro"][i])
        print("  Cidade:", Banco_de_dados["endereço"]["cidade"][i])
        print("  Estado:", Banco_de_dados["endereço"]["Sigla/estado"][i])
        print()
