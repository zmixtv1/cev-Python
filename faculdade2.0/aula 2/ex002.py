lista = []
def menu():
    print("[c] - Create")
    print("[r] - Read")
    print("[u] - Update")
    print("[d] - Delete")
    print("[e] - Exit")
    opção = input("opção: ")
    return opção
def create():
    nome = input("nome: ")
    lista.append(nome)

def read():
    global lista
    print(lista)

def update():
    p = int(input("Qual pisoção: "))
    novo_nome = input("Novo nome: ")
    lista[p] = novo_nome

def delete():
    v = input("Qual nome:")
    