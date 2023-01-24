#Declaração de variáveis de histórico e controle
historico = []
append=0
#Declaração de funções
def operator(operador,a):
 #Gerador de inputs
 if(operador<5):
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
 elif(operador==5):
    x = float(input("Digite o número base: "))
    y = float(input("Digite o número expoente: "))
 else:
    x = float(input("Digite o número desejado: "))
 #Declaração das operações
 if(operador==1):
    z=x+y
    forma="+"
 elif(operador==2):
    z=x-y
    forma="-"
 elif(operador==3):
    z=x*y
    forma="*"
 elif(operador==4):
    z=x/y
    forma="/"
 elif(operador==5):
    z=x**y
    forma="^"   
 elif(operador==6):
    z=math.sqtr(x)
    forma="√"  
 historico.append(f"[{a}] > {x} {forma} {y} = {z}")
 return z
#Main
executor = True   #Variável de execução criando o loop para o algoritimo
while(executor==True):
    #Tela inicial com as opções
    print("===================")
    print("|P.CALC - 2023    |")
    print("+-----------------+")
    print("|1 - Operações    |")
    print("|2 - Histórico    |")
    print("|3 - Sair         |")
    print("===================")
    opcao = int(input("Comando: "))
    while(opcao<=0 or opcao>3):
        opcao = int(input("Opcão inválida. Tete novamente: "))
    # Caso o cliente deseje ver as operações disponíveis
    if(opcao==1):
     #Tela de seleção de operações
     print("+------------------+")
     print("|1 - Somar         |")
     print("|2 - Subtrair      |")
     print("|3 - Multiplicar   |")
     print("|4 - Dividir       |")
     print("|5 - Potencializar |")
     print("|6 - Raiz          |")
     print("+------------------+")
     opcao = int(input("Comando: "))
     while(opcao<=0 or opcao>6):
       opcao = int(input("Opcão inválida. Tete novamente: "))
     append+=1
     #É realizado o comando da função de operações que posteriormente gerará o resultado final
     resultado=operator(opcao,append)
     print("-------------")
     print(f"Seu resultado é: {resultado}")
     print("-------------")
     retorno = input("Tecle enter para retornar ")
    #Caso o pessoa deseje conferir o histórico
    elif(opcao==2):
        for i in historico:
            print(i)
        print("-------------")
        retorno = input("Tecle enter para retornar ")
    #Caso a pessoa deseje encerrar sua sessão
    else:
     executor=False
