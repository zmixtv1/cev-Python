from time import sleep
def ajuda(com):
    print(f"Acessando o manual do comando '{com}'...")
    sleep(2)
    f"\033[0;33m{help(com)}"

def titulo(msg,):
    tam = len(msg)-19
    print("\033[0;36m(～￣▽￣)～" * tam)
    print(f"    {msg}")
    print("\033[0;36m(～￣▽￣)～" * tam)


comando = ""
while True:
    titulo("Sistea de ajuda PyHELP")
    comando = str(input("\033[0;35mFunção ou biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("Até Logo,volte sempre!")