
from operações import *

print (""""
░█████╗░░█████╗░███╗░░██╗████████╗░█████╗░  ██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░██████╗░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░███████║  ██████╦╝███████║██╔██╗██║██║░░╚═╝███████║██████╔╝██║███████║
██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██║  ██╔══██╗██╔══██║██║╚████║██║░░██╗██╔══██║██╔══██╗██║██╔══██║
╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║  ██████╦╝██║░░██║██║░╚███║╚█████╔╝██║░░██║██║░░██║██║██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝""")
 

conta_Usur=0.0
historico=[]
saques=0
while(1):
    print("Escolha uma opção")
    print("1-Deposito")
    print("2-Saque")
    print("3-Extrato")
    print("4-Encerra Sessão")
    x=int(input("Digite o número correspondete a uma dessas operações:"))
    if x==1:
        conta_Usur=deposito(conta_Usur,historico)
    elif x==2:
        if saques>=3:
            print("Já realizou seus saques diarios")
        else:
            conta_Usur=saque(conta_Usur,historico,saques)
            saques+=1
    elif x==3:
        extrato(historico)
    elif x==4:
        print("Até a proxima!")
        break
    else:
        print("OPERAÇÃO INVALIDA")
        