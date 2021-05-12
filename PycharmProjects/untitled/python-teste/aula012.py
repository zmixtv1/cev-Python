nome = str(input("Qual é seu nome? ")).capitalize()
if nome == "Rodrigo":
    print("que bonito seu Nome!!")
elif nome == "Rodrigo" or "Pedro" or "Enzo" or "Maria":
    print("Seu nome é bem popular no Brasil")
elif nome in ("Ana cláudia Jéssica Juliana"):
    print("Belo nome feminino!")
else:
    print("Seu nome é normal!!")
print("tenha um bom dia, {}".format(nome))
