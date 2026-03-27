#lidando com exeções
from logging import exception
import sys
x = int (input("x: "))
y = int (input("y: "))
try:
    resultado = x / y
except ZeroDivisionError:
    print("não é possivel dividir por zero.")
    sys.exit(1)
print(f"o resultado de {x} / por { y} é {resultado}")