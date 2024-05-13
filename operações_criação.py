

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
       
        
        
def Criar_conta():
    global contas
    cpf = input("Qual o seu CPF: ")
    lista2 = verificar2(cpf, banco_de_dados)
    existe, ind = lista2
    if existe:
       print("\033[91mCPF não está cadastrado\033[0m")
    else:
        usur = busca_usuario(banco_de_dados, ind)
        print(f"Olá {usur}, vamos criar uma nova conta para você")
        contas = contas + 1 
        cpf_conta = {cpf: [contas]}
        x = busca_conta_cpf(cpf, lista_contas)
        if x:
            lista_contas[cpf].append(contas)
        else:
            lista_contas.append(cpf_conta)
        print(f"Olá, agência será 0001 conta: {contas}")