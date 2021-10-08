class produto(object):
    def __init__(self,nome, vlr_compra, vlr_venda, vlr_estoque, qtd_minima):
    def get_nome(self):
        







if __name__ == "__main__":
    prod_1 = produto("Arroz", 15.00,19.50,67,20)
    print(prod_1)
    print("Nome: ",prod_1.get_nome())
    print("Qtd. estoque: ",prod_1.ger_qtd_estoque())
    qtd = 22
    prod_1.set_qtd_minima(qtd)
    print("Qtd minima ",prod_1.get_qtd_minima())
    prod_1.set_qtd_minima(33)
    print("Qtd minima ",prod_1.get_qtd_minima())
    print("Nome: ", prod_1.get_nome())
    prod_1.set_nome(15)
    print("Nome: ", prod_1.get_nome())
    prod_1.set_qtd_estoque("Nome")
    prod_1.set_vlr_compra("string")
    print("mostra dados: ",prod_1)