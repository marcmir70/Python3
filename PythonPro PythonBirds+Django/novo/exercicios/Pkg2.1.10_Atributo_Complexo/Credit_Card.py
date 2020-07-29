# do Fórum Python Pro / Python Birds: Atributo Complexo
# baseado no código de marilliviamelo em 20190313_0751h
class Cartao_de_Credito():
    def __init__ (self,*faturas, variante, anuidade):
       self.variante = variante
       self.anuidade = anuidade
       self.faturas = list(faturas)

if __name__ == '__main__':
    fat1 = Cartao_de_Credito('100-8', variante='b',anuidade= 300)
    fat2 = Cartao_de_Credito('101-1', variante='b',anuidade= 300)
    fat3 = Cartao_de_Credito('102-3', variante='b',anuidade= 300)
    fat4 = Cartao_de_Credito('103-5', variante='b',anuidade= 300)
    c = Cartao_de_Credito(fat1, fat2, fat3, fat4, variante='b',anuidade= 300)
    print(c.variante)
    print(c.anuidade)
    print(c.faturas)
    for fat in c.faturas:
        print(f' - {fat.faturas}')