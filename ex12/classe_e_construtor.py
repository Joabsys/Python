#como criar uma classe em python e um metodo automatico " metodo cosntrutor"
#que é executado automaticamente todos vez que um objeto da classe é criado.
#onde self é o mesmo que this do c#
#e def __init__ é o construtor da classe que executa toda vez que um obejto da classe é criado
#armazena o que foi passado no parametro da classe nela mesma.
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Ponto(1,2)
print(p.x)


