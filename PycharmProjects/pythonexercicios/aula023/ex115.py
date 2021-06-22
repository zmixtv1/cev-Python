from lib.interface import *
from lib.arquivo import *
from time import sleep
arq = "arquivo.txt"
if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(["Listar pessoas", "Cadastrar pessoas", "Sair do sistema"])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho("Novo cadastro")
        nome = str(input("Nome: "))
        idade = leiaInt("idade: ")
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mErro! digite uma opção inválida\033[m")
    sleep(1)
