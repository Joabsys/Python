def quadrado (x):
    fat = 1
    for i in range(x, 1, -1):
        fat*=i
    return fat

valor = quadrado(5)
print(f"O valor é:{valor}")