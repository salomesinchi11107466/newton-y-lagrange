

# Desafio 3 : Aproximacion por taylor

Este documento describe la representación de números decimales en binario, una forma en la que las computadoras almacenan valores en bits.

## 📚 Concepto Básico
Para representar un número decimal en binario, utilizamos un espacio de bits, en el que cada bit representa un 1 o un 0. La cantidad de bits necesarios se define como:

\[
m \times b^n
\]

donde:
- \( m \) es el número original convertido a decimal,
- \( b \) es la base numérica (10 para números decimales),
- \( n \) es el número de posiciones desplazadas.

## 🎯 Ejemplo de Conversión
Supongamos que queremos convertir el número **123.123**:
1. **Desplazamos el número**:  
   \( 123.123 \rightarrow 0.123123 \)
2. **Multiplicamos por la base**:  
   \( 0.123123 \times 10 \)
3. **Elevamos por el número de posiciones desplazadas**:  
   \( 0.123123 \times 10^3 \)

## 🖥️ Estructura de 16 Bits en Computadoras
En una representación de 16 bits, cada segmento cumple una función específica:
- **Primer bit**: Signo del número (0 para positivo, 1 para negativo)
- **Segundo bit**: Signo del exponente
- **Bits intermedios**: Representan el exponente
- **Bits finales**: Representan la mantisa (valor decimal ajustado)

Cuando un número es demasiado grande para representarse en el espacio disponible de bits, ocurre un **desbordamiento**.

## 🎯 Ejemplo de Representación en 8 Bits
Para un sistema de 8 bits, el número máximo se representa de la siguiente forma:
1. Convertimos la mantisa y el exponente a decimal.
2. Ejemplo:  
   \( 0.111 \times 2^{111} = 0.875 \times 2^7 = 112 \) (en base decimal).

## ⚙️ Error de Máquina y Ejercicio
Para sistemas de 32 y 64 bits, el **error de máquina** se define como:

\[
\epsilon = 2.22 \times 10^{-16}
\]

En un sistema de 32 bits:
- **7 bits** para el exponente
- **23 bits** para la mantisa
  - **Valor mínimo**: \( 0.5 \times 2^{-256} \)

En un sistema de 64 bits:
- **11 bits** para el exponente
- **52 bits** para la mantisa
  - **Valor máximo**: \( 0.9999997615814209 \times 2^{4194304} \)

---

Este README proporciona una introducción estructurada a cómo las computadoras manejan números decimales en formato binario, detallando la función de cada segmento de bits y algunos ejemplos prácticos.
