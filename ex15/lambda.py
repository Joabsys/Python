
people = [
    {"Nome": "joab", "Casa": "Brasil"},
    {"Nome": "Maria", "Casa": "Argentina"},
    {"Nome": "emily", "Casa": "Alemanha"}]


# def f(pessoa):
#     return pessoa["Nome"]

#vamos substituir a função acima por uma expressão lambda no sort() abaixo
#metodo keys retorna as chaves de um dicionário como uma lista em Python.
# As chaves são retornadas como um objeto especial dict_keys.
#lambdas são expressão usada para criar um função anonima na hora.
people.sort(key=lambda xpeople: xpeople["Casa"])

print(people)

