f1 = str(input("Digite uma frase: "))
f2 = str(input("Digite outra frase: "))

if len(f1) > len(f2):
    print(f1)
else:
    print(f2)

print(f1.upper())
print("Banana " + f1 + " Acabou")

for c in range(0, len(f1)):
    frase1 = f1
    if frase1.isalnum():
        print("tem um numero!")
    elif f1.isalpha():
        print("não tem um numero!")
