
from abc import ABC
from datetime import datetime
from bancodedados import*
from bancodedados import usuarios

  
class PessoaFisica():
    def __init__(self,cpf,nome,data_nascimento,endereco):
        self.cpf=cpf
        self.nome=nome
        self.data_nascimento=data_nascimento
        self.endereco=endereco
        
class Cliente(PessoaFisica):
    lista_contas=[]#dentro de lista dever ter um dicionario com argumentos de numero de conta,agencia,saldo
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento, endereco)
    def realizar_transacao(conta,transacao):
        #Nesse metodo ira modificar uma conta e resgstrar as modificações gerando um numero de transação
        pass
    def adicionar_conta(conta,cpf):
        #irar adicionar um conta para um cliente , o argumento conta é so devido o desafio
        pass
class conta ():
    def __init__(self,cpf,conta):
        #para modificar uma conta de cliente na lista de conta do cliente 
        self.cpf=cpf
        self.conta=conta
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print("Valor do saque é maior do que o saldo")
        elif valor >0:
            self._saldo -=valor
            print("Saque realizado com sucesso")
            return True
        else:
            print("Operação falhou")
            return False

    def depositar(self, valor):
        saldo = self.saldo
        if valor >0:
            self._saldo -=valor
            print("DEpositor realizado com sucesso")
            
        else:
            print("Operação falhou")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print(" Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print(" Operação falhou! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """



class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)










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