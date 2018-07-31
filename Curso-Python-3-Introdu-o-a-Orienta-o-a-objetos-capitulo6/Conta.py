class Conta:
    
    #Self faz referencia ao objeto... É como se fosse o this do javascript;
    def __init__(self, numero, titular, saldo, limite): 
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite #atributos privados

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    # método privado, só pode ser usado dentro da classe.
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular
    #conta.limite
    # Certo, usar property é uma ótima prática. 
    # Quando criamos getters e setters todos os lugares que
    #  já acessam a classe precisam mudar.
    @property
    def limite(self):
        return self.__limite
    
    #forma de chamar - > conta.limite = 2000
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    #conta = Conta.codigo_banco()
    @staticmethod #Método estático da classe. Para acessar tem que ser direto com o nome da class, que nem no JAVA.
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}