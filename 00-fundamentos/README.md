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

### ¿Qué es un logaritmo, en criollo?

`log_b(x) = y` significa: **«¿a qué potencia tengo que elevar `b` para obtener `x`?»**, o sea `b^y = x`. Es la operación inversa de la exponencial. Ejemplos: `log10(1000) = 3` porque `10^3 = 1000`; `log2(8) = 3` porque `2^3 = 8`.

El logaritmo cuenta órdenes de magnitud: cada vez que multiplicas por 10, el logaritmo en base 10 solo sube 1. Por eso achica rangos enormes a números manejables. En IA aparece en el *loss* (entropía cruzada): `-log(p)` castiga mucho una predicción muy segura y equivocada (`-log(0.1) = 2.3`) y poco una casi correcta (`-log(0.9) = 0.105`).

**Ojo en NumPy:** `np.log` es el logaritmo natural (base `e ≈ 2.718`, se escribe `ln`). `np.log10` es base 10 y `np.log2` es base 2.

### Propiedades fundamentales

1. **Producto → suma:** `log(a·b) = log(a) + log(b)`. La más importante en IA: convierte la verosimilitud (un producto gigante de probabilidades) en una suma.
2. **Cociente → resta:** `log(a/b) = log(a) − log(b)`.
3. **Potencia → multiplicación:** `log(a^n) = n·log(a)`. La potencia baja a multiplicar.
4. **Los dos valores base:** `log(1) = 0` y `log(b) = 1` (el log de la propia base es 1).
5. **Cambio de base:** `log_b(x) = ln(x) / ln(b)`. Cualquier logaritmo se calcula con el natural.
6. **Son inversos:** `b^(log_b(x)) = x` y `log_b(b^x) = x`. Se cancelan mutuamente.
7. **Dominio:** solo existe para `x > 0`. `log(0)` no existe (tiende a `-infinito`) y el log de un negativo no existe en los reales.
8. **Mantiene el orden (base > 1):** si `a > b`, entonces `log(a) > log(b)`. Por eso maximizar el logaritmo de algo es lo mismo que maximizar ese algo: así se entrena por máxima verosimilitud.

## 4. NumPy: el Excel con esteroides de Python

Un array de NumPy es una lista, pero con matemática vectorizada: sumas, multiplicas y operas sobre miles de números de una sola vez, sin `for`. Todo el repo corre sobre esto. Si dominas `np.array`, `np.dot` y el *broadcasting* (operar un vector con un número), ya tienes el 80% de la herramienta.

Corre `python_numpy.py` y cambia los números para ver qué pasa.
