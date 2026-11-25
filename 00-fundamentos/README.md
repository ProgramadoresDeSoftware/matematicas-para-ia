# 00 — Fundamentos: lo que hay que tener fresco

Antes de vectores y derivadas, cuatro herramientas que vas a usar en todos los módulos. Nada nuevo si programaste, pero aquí con el significado que importa en IA.

## 1. Funciones: máquinas que transforman un número en otro

`f(x) = 2x + 1`. Entra `x`, sale otro número. Un modelo de IA es eso, pero gigante: entran miles de números, salen otros miles. Todo lo demás es decoración.

En código, una función es una función. La gracia es pensar así: **modelo = función con parámetros que se aprenden**.

## 2. Sumatoria (Σ): "suma todo esto"

`Σ x_i` significa: suma todos los `x`. Cuando veas una fórmula con Σ, no te asustes: es un `for` que suma. El error de un modelo, por ejemplo, es casi siempre una suma de errores pequeños.

## 3. Exponencial (e^x) y logaritmo (log): crecer y achicar

- `e^x` crece rapidísimo. Aparece en softmax y en probabilidades.
- `log(x)` es lo contrario: achica números enormes para poder compararlos. El "loss" de un modelo casi siempre lleva un log.
- Regla que vale oro: `log(a * b) = log(a) + log(b)`. Convertir multiplicaciones en sumas es lo que hace computable casi todo en IA.

## 4. NumPy: el Excel con esteroides de Python

Un array de NumPy es una lista, pero con matemática vectorizada: sumas, multiplicas y operas sobre miles de números de una sola vez, sin `for`. Todo el repo corre sobre esto. Si dominas `np.array`, `np.dot` y el *broadcasting* (operar un vector con un número), ya tienes el 80% de la herramienta.

Corre `python_numpy.py` y cambia los números para ver qué pasa.
