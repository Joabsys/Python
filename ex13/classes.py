class Voo:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiro = []

    def add_passageiro(self, nome):
        if not self.acentos_abertos():
            return False
        self.passageiro.append(nome)
        return True

    def acentos_abertos(self):
        return self.capacidade - len(self.passageiro)


voo = Voo(3)
pessoas = ["maria","joab","emily","Geize"]
for pessoa in pessoas:
    if  voo.add_passageiro(pessoa):
        print(f"{pessoa} adicionada ao voo com sucesso.")
    else:
        print(f"{pessoa} não adicionada ao voo.")

