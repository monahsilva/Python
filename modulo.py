class Conta_corrente(object):
        def __init__(self, nome_pessoa,numero_conta, saldo = 0):
                self.nome_pessoa = nome_pessoa
                self.numero_conta = numero_conta
                self.saldo = saldo

        def alterar_nome(self,nome_atual,numero_atual):
                self.nome_pessoa = nome_atual
                self.numero_conta = numero_atual
                print("Operação realizada com sucesso!!!")
                print("A nova conta é : {0}".format(nome_atual))
                print("Com o numero: {0}".format(numero_atual))
                
        def depositar(self, deposito):
                self.saldo += deposito
                print("Operação realizada com sucesso!!!")
                print("Seu saldo é: {}".format(self.saldo))

        def sacar(self, saque):
                if self.saldo < 0:
                        print("Impossivel realizar saque!!!")
                        print("Seu saldo é: {}".format(self.saldo))
                elif self.saldo < saque:
                        print("Dinheiro não disponivel!!!")
                        print("Seu saldo é: {}".format(self.saldo))
                else:
                        self.saldo -= saque
                        print("Operação realizada com sucesso!!!")
                        print("Seu saldo é: {}".format(self.saldo))