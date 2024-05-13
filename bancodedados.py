usuarios=0
contas=0
lista_contas=[]
banco_de_dados=[]

def verificar(usuariocpf, bancodedados):
    for entrada in bancodedados:
        cpf = entrada["cpf"]
        if cpf == usuariocpf:
            return False
    else:
        return True
    
def verificar2(usuariocpf, bancodedados):
    for indice,entrada in enumerate(bancodedados):
        cpf = entrada["cpf"]
        if cpf == usuariocpf:
            return False,indice
    else:
        return True,None





def busca_usuario(bancodedados,indice):
    usur=bancodedados[indice]["nomes"]
    return usur
def busca_conta_cpf(cpf2, bancos):
    for x in bancos:
        if x == cpf2:
            return True
        else:   
            return False

        