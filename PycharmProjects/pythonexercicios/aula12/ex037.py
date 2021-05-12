n1 = int(input("Me diga Qual o numero você quer converter? "))
print("Qual base de conversão você quer:\n[1] converter para BINÁRIO\n[2] converter para OCTAL\n[3] converter para HEXADECIMAL")
base = input("Sua opção: ")

if base == "1":
    print("{} convertido para BINÁRIO é {}".format(n1, bin(n1)[2:]))
elif base == "2":
    print("{} convertido para OCTAL é {}".format(n1, oct(n1)[2:]))
elif base == "3":
    print("{} convertido para HEXADECIMAL é {}".format(n1, hex(n1)[2:]))
else:
    print("Opção invalida!")

