from time import sleep
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))
escolha = 0
while escolha != 5:
    print("------------Qual tipo de operação:------------")
    print("[ 1 ]SOMAR\n[ 2 ]MULTIPLICAR\n[ 3 ]MAIOR\n[ 4 ]NOVOS NÚMEROS\n[ 5 ]SAIR DO PROGRAMA")
    escolha =int(input("Qual é sua opção? "))
    if escolha == 1:
        soma = valor1 + valor2
        print("A soma dos valores {} + {} é {}".format(valor1, valor2, soma))
    elif escolha == 2:
        mult = valor1 * valor2
        print("A multiplicação entre {} x {} é {}".format(valor1, valor2, mult))
    elif escolha == 3:
        if valor1 > valor2:
            print("O valor {} é maior que o {}".format(valor1, valor2))
        elif valor1 == valor2:
            print("Os valores digitados ({}, {}) são iguais!".format(valor1, valor2))
        else:
            print("O valor {} é maior que o {}".format(valor2, valor1))
    elif escolha == 4:
        print("=-" * 23)
        print("Digite os numero novamente:")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif escolha == 5:
        print("Finalizando...")
        sleep(1)
    else:
        print("opção invalida!")
    sleep(1)
print("---------------Fim-do-programa----------------")