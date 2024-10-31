Aquí tienes una versión compacta y detallada para el README:

---

# Propagación de Errores 

Cuando una función depende de varias variables aproximadas, los errores individuales en estas variables también afectan al valor resultante. Dada una función \( y = f(x_1, x_2, \dots, x_n) \), donde cada variable \( x_i \) tiene un error asociado \( \Delta x_i \), el error en \( y \) (\( \Delta y \)) se puede calcular a partir de las derivadas parciales de \( f \) respecto a cada variable:

\[
\Delta y = \left| \frac{\partial y}{\partial x_1} \Delta x_1 \right| + \left| \frac{\partial y}{\partial x_2} \Delta x_2 \right| + \dots + \left| \frac{\partial y}{\partial x_n} \Delta x_n \right|
\]

### 🎯 Ejemplo: Cálculo de Errores en una Fórmula Física

Supongamos la fórmula de transferencia de calor:

\[
H = A \cdot e \cdot \sigma \cdot T^4
\]

con los valores:
- \( A = 0.15 \pm 0.1 \)
- \( e = 0.9 \pm 0.01 \)
- \( \sigma = 5.67 \times 10^{-8} \)
- \( T = 650 \pm 40 \)

El error total en \( H \) (\( \Delta H \)) se calcula como:

\[
\Delta H = \left| e \cdot \sigma \cdot T^4 \Delta A \right| + \left| A \cdot \sigma \cdot T^4 \Delta e \right| + \left| A \cdot e \cdot \sigma \cdot 4 T^3 \Delta T \right|
\]

### Resultado

Con los valores de \( A \), \( e \), \( \sigma \), y \( T \) sustituidos, obtenemos que:
- **\( H \approx 1366.38 \)**
- **\( \Delta H \approx 274.44 \)**

Este README resume el cálculo de errores en función de los errores de variables independientes, proporcionando un ejemplo para facilitar su comprensión y aplicación.
