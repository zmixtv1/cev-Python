from lib.interface import *
from lib.arquivo import *
from time import sleep
arq = "arquivo.txt"
if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(["Listar pessoas", "Cadastrar pessoas", "Sair do sistema"])
    if resp == 1:
        cabeçalho("opção 1")
    elif resp == 2:
        cabeçalho("Opção 2")
    elif resp == 3:
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mErro! digite uma opção inválida\033[m")
    sleep(2)
