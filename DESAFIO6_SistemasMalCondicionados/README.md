

# 🏁 Interpolación

La **interpolación** es una técnica que permite definir una función general con base en ciertos valores conocidos, similar a la regresión lineal. Es útil para estimar valores intermedios entre puntos conocidos en un conjunto de datos.

### 📌 Nota

Para realizar interpolación, se necesitan dos conjuntos de valores relacionados (\( x \), \( y \)), que conforman una tabla de referencia:

| Variable \( x \) | Variable \( y \) |
|------------------|------------------|
| 1                | 1                |
| 2                | 3                |
| ...              | ...              |

## 🧪 Método de Lagrange

El **Método de Lagrange** genera un polinomio que interpola entre valores mediante el uso de productos y sumas de términos conocidos. La fórmula para la función de Lagrange \( L_i(x) \) es:

\[
L_i(x) = \prod_{j \neq i} \frac{x - x_j}{x_i - x_j}
\]

Para cada valor \( x \) en la tabla, creamos una función \( L_i(x) \). Luego, usamos estas funciones en el polinomio de interpolación de Lagrange:

\[
P(x) = \sum_{i=0}^n L_i(x) \cdot y_i
\]

Es decir, multiplicamos cada función de Lagrange \( L_i(x) \) por su valor correspondiente \( y_i \). Esta suma genera el valor interpolado en cualquier \( x_k \).

### 💡 Sugerencia

Dado que el método de Lagrange puede ser largo y complejo, se suele usar solo los puntos cercanos al valor deseado \( x_k \) para facilitar el cálculo.

### 🎯 Ejemplo de Interpolación en MATLAB/Octave

Para interpolar un valor específico \( x_k \) en MATLAB u Octave:

```matlab
% Definir los valores
x = [1, 2, 3, 4, 5, 6, 7];
y = [3, 4, 5, 6, 7, 8, 9];

% Definir el valor a calcular
xk = 3.3;

% Realizar la interpolación
yk = interp1(x, y, xk);

% Interpolar un conjunto de valores
xk_2 = 1:0.1:7;
yk_2 = interp1(x, y, xk_2);

% Graficar la función
plot(x, y);
```

Ahora tenemos una función lista para interpolar cualquier valor de \( x_k \), solo necesitamos cambiar \( x_k \) para obtener su correspondiente \( y_k \).

### 📌 Nota

La función `interp1` permite realizar interpolación en MATLAB y Octave. Esta función requiere al menos tres parámetros: los valores \( x \) y \( y \), y el valor \( x_k \), que puede ser uno o varios valores.

Para mejorar la precisión de la interpolación, `interp1` acepta un cuarto parámetro que especifica el método de interpolación, como `'spline'` o `'pchip'`.

### ⚠️ Advertencia

Existen diferentes enfoques dentro de un mismo método de interpolación, y cada uno puede ofrecer variaciones en precisión. ¡Selecciona el método adecuado para tu caso específico!


