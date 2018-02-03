from modulo import Conta_corrente

def main():
        print("Processando...... \n")
        nome_pessoa = input("Entre com o nome do correntista: ")
        numero_conta = input("Entre com o numero da conta: ")
        op = eval(input("Deseja informar o saldo? 1-Sim 2-Não \n"))

        if op == 1:
                saldo = eval(input("Digite o saldo: "))
                conta = Conta_corrente(nome_pessoa,numero_conta, saldo)
        elif op == 2:
                print("OK!")
                conta = Conta_corrente(nome_pessoa,numero_conta) #nao mandei o saldo pois a propria classe ira atribuir
        else:
                print("Opção Invalida!!!!!!!")

        op = eval(input("1-Saque, 2-Deposito , 3-Alterar nome \n"))

        if op == 1:
                valor = eval(input("Entre com o valor a ser retirado: "))
                conta.sacar(valor)
        elif op == 2:
                value = eval(input("Entre com o valor a ser depositado: "))
                conta.depositar(value)
        elif op == 3:
                nome_atual_pessoa = (input("Entre com o novo nome do correntista: "))
                numero_atual_conta = (input("Entre com o numero nome da conta: "))
                conta.alterar_nome(nome_atual_pessoa,numero_atual_conta)
        else:
                print("Opção Invalida!!!!! ")
                print("Não foi possivel realizar a operação!!!")

        print("Obrigada por comparecer no meu banco!!")
                
if __name__ == '__main__':
        print("Banco Monalisa!!!!!!!!")
        main()
