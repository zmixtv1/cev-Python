num = int(input("Digite um numero: "))
for c in range(0, num + 1):
    if num % c == 0:
        print("\033[34m", end="")
    else:
        print("\033[m", end="")
    print("{}".format(c), end=" ")
