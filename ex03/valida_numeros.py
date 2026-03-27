# o int faz um cast no input,pois o input acha que é uma string
#então usamos o int para converter o input no tipo desejado.

numero = int(input("Digite um numero: "))
if numero > 0:
    print("o numero é positivo.")
elif numero < 0:
    print(" o numero é negativo.")
else:
    print(" o numero é zero.")