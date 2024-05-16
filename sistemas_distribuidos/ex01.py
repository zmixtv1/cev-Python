import threading
import time

class Balde:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.quantidade = 0
        self.mutex = threading.Lock()
        self.lavador_contagem = 0

    def encher(self):
        while self.quantidade < self.capacidade:
            with self.mutex:
                if self.quantidade + 3 <= self.capacidade:
                    self.quantidade += 3
                    print(f"Ajudante encheu o balde. Quantidade atual: {self.quantidade}")
                else:
                    print("Balde está cheio. Aguardando...")
                    time.sleep(2)

    def esvaziar(self):
        while self.quantidade > 0:
            with self.mutex:
                if self.quantidade >= 10:
                    self.quantidade -= 10
                    self.lavador_contagem += 1 
                    print(f"Lavador esvaziou o balde. Quantidade atual: {self.quantidade}")
                    time.sleep(3) 
                else:
                    print("Balde está vazio.")
                    break

balde = Balde(100)

def ajudante_encher():
    balde.encher()

def lavador_esvaziar():
    balde.esvaziar()


ajudante1 = threading.Thread(target=ajudante_encher)
ajudante2 = threading.Thread(target=ajudante_encher)
ajudante3 = threading.Thread(target=ajudante_encher)
lavador = threading.Thread(target=lavador_esvaziar)


ajudante1.start()
ajudante2.start()
ajudante3.start()
lavador.start()


ajudante1.join()
ajudante2.join()
ajudante3.join()
lavador.join()

print(f"O lavador foi ao balde {balde.lavador_contagem} vezes para esvaziá-lo.")
print("Processo concluído.")
