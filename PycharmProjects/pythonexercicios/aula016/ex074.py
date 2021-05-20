from random import randint
núm = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
print("Eu sortei esses numeros: " , end="")
for n in núm:
    print(f"{n}", end=" ")

print(f"\nO maior valor sorteado foi: {max(núm)}")
print(f"O menor valor sorteado foi: {min(núm)}")