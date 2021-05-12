
while True:
    tabuada = int(input("Quer ver a tuabuada de qual valor? "))
    print("_"*15)
    if tabuada < 0:
        break
    for c in range(1, 11):
        valor = tabuada * c
        print(f"{tabuada} x {c} = {valor}")
    print("_"*15)
print("Programa de tabuada encerrado, volte sempre.")
