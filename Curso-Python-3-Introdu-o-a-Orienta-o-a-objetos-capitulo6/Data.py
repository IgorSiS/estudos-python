class Data:
    #pass  - > terminei.. e posso criar objeto. Deixar passar.
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes,self.ano))