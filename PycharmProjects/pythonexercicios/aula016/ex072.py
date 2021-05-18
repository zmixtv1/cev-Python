cont = ("zero", "Um", "Dois", "Tres", "Quatro",
          "Cinco", "Seis", "Sete", "Oito",
          "Nove", "Dez", "onze", "Doze",
          "Treze", "Catorze", "Quinze", "dezesseis",
          "dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    num = int(input("Digite um numero entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    print("tente novamente", end="")
print(f"Você digitou o numero {cont[num]}")
