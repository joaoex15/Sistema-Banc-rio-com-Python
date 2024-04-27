


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
