import matplotlib.pyplot as plt
import numpy as np


# Paso 1: Representación binaria
binary_mantissa = '0.1111'
exponent = 11

# Convertir la mantisa binaria a decimal
mantissa_decimal = float(int(binary_mantissa.replace('.', ''), 2)) / (2 ** len(binary_mantissa.split('.')[1]))

# Multiplicar por 2^11
original_value = mantissa_decimal * (2 ** exponent)

# Mostrar el valor original en binario
original_binary = bin(int(original_value))[2:]

# Paso 2: Convertir a decimal
decimal_value = original_value

print(f'Valor original en binario: {original_binary}')
print(f'Valor en decimal: {decimal_value}')
