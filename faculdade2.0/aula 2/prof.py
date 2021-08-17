lista = []                      # Lista vazia
def menu():
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input('Opção: ')
    return opcao
# - A função create não recebe nada e não retorna nada. Lê um nome e insere na lista.
def create():
    nome = input('Nome: ')
    lista.append(nome)
# - A função read não recebe nada e não retorna nada. Mostra todos os itens da lista.
def read():
    print(lista)                        # Na horizontal
''' - A função update não recebe nada e não retorna nada. Lê os dados necessários pra atualizar
(índice e o novo nome) e substituir (alterar) um item da lista.                       '''
def update():
    p = int(input("Qual posição: "))
    novo_nome = input("Novo nome: ")
    # Usando notação de vetor:              Sintaxe: nome_lista[indice] = novo_nome
    lista[p] = novo_nome                    # Solução 1, notação vetor.
    # lista.pop(p)                          # Solução 2, funções de lista.
    # lista.insert(p, novo_nome)            # Solução 2
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

