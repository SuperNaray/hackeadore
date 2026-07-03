import time #bibliotecas#
import sys
print("hackeadore v1.0 beta ") #inicio do programa
print("________________________________")
print("escolha uma das opções abaixo")
print("hackear wi-fi do visinho[1]")
print("atacar os satelites da NASA[2]")
print("desmantelar pedofilos[3]")
print("sair[4]")
resposta = int(input(""))
print("_________________________________")
#condições #se a resposta for 1
if resposta == 1:
    print("hackeando o wi-fi")
    print("descriptografando a senha")
    time.sleep(5)
    print("tentando acesar o wi-fi")
    time.sleep(3)
    print("falhou ao tentar conectar")
    time.sleep(2)
    print("tentando se conectar dnv, aguarde um tempo")
    time.sleep(20)
    print("pronto você está conectado a rede")
    time.sleep(5)
    sys.exit()
#se a resposta for 2
if resposta == 2:
    print("você escolheu hackear a NASA a opção mais dificil e mais demorada")
    time.sleep(5)
    print("tentando acessar o banco de dados")
    time.sleep(20)
    print("aceso concedido aos servidores da nasa")
    time.sleep(2)
    print("tentando conectar ao satelite mais proximo (essa ação vai ser  demorada)")
    time.sleep(60)
    print("acesso ao satelite mais proximo foi um sucesso")
    time.sleep(2)
    print("tantando se conectar a todos os satelites da NASA")
    time.sleep(5)
    print("falhou ao tentar conectar")
    print("tentando conectar denovo")
    time.sleep(10)
    print("conectado aos satelites da nasa")
    print("destruindo Eua")
    time.sleep(10)
    print("Eua destruido, parabens sem tramp para explodir o mundo")
    time.sleep(3)
    sys.exit()
#se a resposta for 3
if resposta == 3:
    print("destroimos todos os pedofilos em 0.000000001 segundo")
    time.sleep(3)
    sys.exit()
#saida
if resposta == 4:
    sys.exit()

