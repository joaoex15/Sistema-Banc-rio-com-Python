

from bancodedados import*
from bancodedados import usuarios

def Add_Client():
    global usuarios
    Cpf=input("Qual é seu cpf:")
    resultado_consulta=verificar(Cpf,banco_de_dados)
    if resultado_consulta!=True:
        print("\033[91mCpf já cadastrado\033[0m")
    else:
        Name=input ("Nome do cliente:")
        Data_Nasc=input("Data de nascimento:")
        print("Qual seu enderenço completo: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número da casa: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite a sigla do estado: ")


        usario ={
                "nomes": Name,
                "Data_nasc": Data_Nasc,
                "cpf": Cpf,
                "endereço": {
                    "Logradouro": logradouro,
                    "Nro": numero,
                    "bairro": bairro,
                    "cidade": cidade,
                    "Sigla/estado": estado
                }
            }

        lista_cpf.append(Cpf)
        banco_de_dados.append(usario)
        usuarios=usuarios+1
        print("Nome:", usario["nomes"])
        print("Data de Nascimento:", usario["Data_nasc"])
        print("CPF:", usario["cpf"])
        print("Endereço:")
        print("  Logradouro:", usario["endereço"]["Logradouro"])
        print("  Número:", usario["endereço"]["Nro"])
        print("  Bairro:", usario["endereço"]["bairro"])
        print("  Cidade:", usario["endereço"]["cidade"])
        print("  Estado:", usario["endereço"]["Sigla/estado"])
        print(usuarios)
        
        
def Criar_conta():
    cpf=("Qual o seu Cpf:")
    existe,ind=verificar(cpf,banco_de_dados)
    if existe==True:
       print("\033[91mCpf não está cadastrado\033[0m")
    else:
        usur=busca_usuario(banco_de_dados,ind)
        print(f"Olá {usur} vamos criar uma nova conta para você")
        contas=contas+1
        cpf_conta={cpf:[contas]}
        print(f"Olá,agência será 0001 conta:{contas}")