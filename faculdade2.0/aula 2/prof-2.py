lista = []                      # Lista vazia
from time import sleep
'''
def menu():
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input('Opção: ')
    return opcao
'''
def menu():
    while True:
        l_opcoes = ('c','r','u','d','e')
        print('[c] - Create')
        print('[r] - Read')
        print('[u] - Update')
        print('[d] - Delete')
        print('[e] - Exit')
        opcao = input('Opção: ').lower()

        if opcao not in l_opcoes:
            print("Opção invalida, tente novamente")
            sleep(2)
        else:

            break
    return opcao


# - A função create não recebe nada e não retorna nada. Lê um nome e insere na lista.
def create():
    nome = input('Nome: ')
    lista.append(nome)
# - A função read não recebe nada e não retorna nada. Mostra todos os itens da lista.
def read():
    if lista != []:
        for i,v in enumerate(lista):
            print(f"{i} - {v}")
    else:
        print("Lista Vazia!")


''' - A função update não recebe nada e não retorna nada. Lê os dados necessários pra atualizar
(índice e o novo nome) e substituir (alterar) um item da lista.                       '''


def update():
    if lista != []:
        try:
            p = int(input("Qual posição"))
            novo_nome = input("Novo nome: ")
        except ImportError as e:
            print("Erro IndexError: \n" ,e)
        except Exception as e:
            print("Erro Exception\n", e)
    else:
        print("lista Vazia.")


''' - A função delete não recebe nada e não retorna nada. Lê o item (nome) que será
excluído da lista.                                                         '''



def delete():
    v = input("Qual nome: ")
    lista.remove(v)






if __name__ == '__main__':          # Atalho: mai <tab>
    while True:
        op = menu()                 # A variável op recebe o valor que a função menu retorna
        if op == 'c':
            create()                # Chama a função create
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        else:
            break

