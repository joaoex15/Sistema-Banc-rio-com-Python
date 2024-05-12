usuarios=0
contas=0
lista_contas=[]
banco_de_dados=[]

def verificar(usuariocpf, bancodedados):
    for indice,entrada in enumerate(bancodedados):
        cpf = entrada["cpf"]
        if cpf == usuariocpf:
            return False,indice
    else:
        return True,None
def busca_usuario(bancodedados,indice):
    usur=bancodedados[indice]["nome"]
    return user
def busca_conta_cpf(cpf,bancos):
    for x in bancos.keys:
        if x==cpf:
            return True
        else:
            return False
        