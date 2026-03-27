#decoradores permitem que  se altere o retorno de uma função
#passando um função como parametro.
def decorador(f):
    def inicio():
        print("iniciando a função...")
        f()
        print("fim")
    return inicio


@decorador
def hello():
    print("ola, mundo!")
#chamando a função hello
hello()
