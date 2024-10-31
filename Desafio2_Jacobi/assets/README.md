

# 🐫 Método de Jacobi

El **Método de Jacobi** es un algoritmo iterativo para resolver sistemas de ecuaciones lineales. Este método transforma el sistema original para hallar la solución mediante iteraciones en una matriz diagonalmente dominante.

## 📝 ¿Cómo funciona?

1. Dado un sistema de ecuaciones lineales representado en forma matricial:
   \[
   A \cdot x = b
   \]

2. **Verificación de Diagonalidad Dominante**: Comprobamos que la matriz \( A \) es diagonalmente dominante, es decir:
   \[
   |a_{ii}| > \sum_{j=1, j \neq i}^{n} |a_{ij}|
   \]

3. **Reescritura del Sistema**: Se reescribe el sistema en función de cada variable en la diagonal:
   \[
   x = M \cdot x + c
   \]

4. **Cálculo de Convergencia**: Obtenemos los elementos alfa de la matriz \( M \) para garantizar la convergencia, asegurando que el valor máximo de estos elementos sea menor que 1.

### 🎯 Ejemplo de Aplicación

Consideremos el sistema de ecuaciones:

\[
3x_1 - x_2 + x_3 = 1
\]
\[
3x_1 + 6x_2 + 2x_3 = 0
\]
\[
3x_1 + 3x_2 + 7x_3 = 4
\]

Escribimos este sistema en forma matricial:

\[
\begin{bmatrix} 3 & -1 & 1 \\ 3 & 6 & 2 \\ 3 & 3 & 7 \end{bmatrix} \times \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \\ 4 \end{bmatrix}
\]

**Paso 1: Comprobación de Diagonalidad Dominante**

La matriz es diagonalmente dominante porque se cumple:

- \(|3| > |-1| + |1|\)
- \(|6| > |3| + |2|\)
- \(|7| > |3| + |3|\)

**Paso 2: Reescribir en Función de las Variables**

Despejamos cada ecuación en función de \(x_1\), \(x_2\) y \(x_3\):
\[
x_1 = \frac{1}{3} + \frac{1}{3}x_2 - \frac{1}{3}x_3
\]
\[
x_2 = 0 - \frac{1}{6}x_1 - \frac{1}{3}x_3
\]
\[
x_3 = \frac{4}{7} - \frac{3}{7}x_1 - \frac{3}{7}x_2
\]

Reescribimos el sistema en función de la matriz de coeficientes:

\[
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 0 & \frac{1}{3} & -\frac{1}{3} \\ -\frac{1}{6} & 0 & -\frac{1}{3} \\ -\frac{3}{7} & -\frac{3}{7} & 0 \end{bmatrix} \times \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} + \begin{bmatrix} \frac{1}{3} \\ 0 \\ \frac{4}{7} \end{bmatrix}
\]

**Paso 3: Cálculo de los Elementos Alfa para la Convergencia**

Calculamos los alfas (\( \alpha_1, \alpha_2, \alpha_3 \)) para cada ecuación y confirmamos que son menores que 1:
- \(\alpha_1 = \frac{2}{3}\)
- \(\alpha_2 = \frac{1}{6}\)
- \(\alpha_3 = \frac{3}{7}\)

Como todos los alfas son menores que 1, el sistema converge.

### 📦 Proceso de Iteración

1. Inicializamos los valores \( x_1, x_2, x_3 \) (por ejemplo, todos en 0).
2. Sustituimos estos valores en la ecuación iterativa \( x = M \cdot x + c \).
3. Repetimos el paso hasta alcanzar la convergencia y obtener la solución deseada.


