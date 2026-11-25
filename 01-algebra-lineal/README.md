# 01 — Álgebra lineal: cómo "piensa" un modelo con números

Este es **el módulo más importante del repo**. Si solo hicieras uno, que sea este.

## 1. Un vector es una lista de números con dirección

`[3, 4]` no es solo dos números: es una flecha que apunta a algún lado y tiene un largo (su **norma**: `sqrt(3² + 4²) = 5`). En IA, una palabra, una imagen o un usuario entero se representan como un vector: eso es un **embedding**. Dos cosas parecidas tienen vectores parecidos.

## 2. El producto punto mide parecido

`a · b = a₁b₁ + a₂b₂ + ...`. Si da grande, los vectores apuntan al mismo lado: son parecidos. Si da 0, son perpendiculares: no tienen nada que ver. Esto es lo que hace un buscador semántico, un sistema de recomendación y la atención de un transformer: **comparar vectores con producto punto**.

También existe la **similitud coseno**: el producto punto dividido entre los largos. Es el parecido sin importar el tamaño.

## 3. Una matriz es una transformación

Una matriz `M` aplicada a un vector `v` (`M @ v`) mueve, estira o rota esa flecha. Una capa de una red neuronal es exactamente eso: una matriz (los **pesos**) que transforma el vector de entrada en otro vector. Entrenar es encontrar la matriz correcta.

## 4. Sistemas lineales, inversa y determinante (en criollo)

- Resolver `M @ x = b` es preguntar: "¿qué vector, al transformarlo con M, me da b?"
- La **inversa** `M⁻¹` es la transformación que deshace a M. No todas las matrices la tienen.
- El **determinante** dice cuánto estira o encoge la transformación (y si aplasta todo a cero: determinante 0 = la matriz pierde información).

## 5. Autovalores, autovectores y SVD (la idea, sin susto)

- Un **autovector** es una dirección que la matriz no cambia de dirección, solo estira o encoge. El cuánto estira es el **autovalor**.
- La **SVD** descompone cualquier matriz en tres piezas simples. Es la herramienta detrás de PCA (reducir dimensiones) y de LoRA (entrenar barato un modelo grande). La idea basta por ahora; el detalle vive en el módulo 05.

Corre `vectores_matrices.py`, cambia los vectores y mira cómo cambia el parecido.

## Glosario rápido: las funciones que usaste

| Función | Qué es, en criollo | Qué devuelve |
|---|---|---|
| `np.linalg` | La caja de herramientas de álgebra lineal de NumPy. `linalg` = *linear algebra*. No hace nada sola: es el apellido de `det`, `solve`, `norm`, `inv`, `eig`… | — |
| `np.linalg.det(M)` | El **determinante**: un solo número que dice cuánto estira o encoge la matriz. `det = 0` significa que aplasta todo a una línea o un punto: sin inversa, sin solución única. | Un número |
| `np.linalg.solve(M, b)` | Resuelve `M @ x = b`: «¿qué vector, al transformarlo con M, me da b?». Exige matriz cuadrada con `det ≠ 0`; si no, explota con `LinAlgError: Singular matrix`. | El vector `x` |
| `np.dot(a, b)` | El **producto punto**: multiplica elemento a elemento y suma todo. Con vectores mide parecido de dirección; con matrices 2D es multiplicación de matrices (hoy se prefiere `@` o `np.matmul` para eso). | Un número (vectores) o una matriz |
| `np.linalg.norm(v)` | La **norma**: el largo de la flecha. `norm([3, 4]) = 5`. | Un número |

## Dónde buscar documentación básica

1. **Dentro del propio Colab (lo más rápido):** escribe `np.linalg.det?` o `help(np.dot)` en una celda y corre. También `Shift + Tab` con el cursor sobre la función muestra su ayuda sin salir del notebook.
2. **Documentación oficial de NumPy (en inglés, con ejemplos):** [Linear algebra — NumPy Manual](https://numpy.org/doc/stable/reference/routines.linalg.html). Ahí están `dot`, `det`, `solve`, `norm` y todas las demás, cada una con su página propia y ejemplos que se pueden copiar a Colab.
3. **Este repo:** cada README explica primero en criollo qué hace la función y por qué importa en IA, antes de la fórmula.
