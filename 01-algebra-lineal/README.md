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
