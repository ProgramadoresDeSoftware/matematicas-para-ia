# 04 — Optimización: bajar el error, paso a paso

## La idea en criollo

Entrenar es bajar una montaña (la función de error) con los ojos vendados, sintiendo la pendiente con los pies. El **descenso de gradiente** es el método: mira la pendiente, da un pasito en sentido contrario, repite miles de veces.

## Lo que vas a aprender aquí

- Descenso de gradiente, tasa de aprendizaje y por qué importa tanto.
- SGD (gradiente estocástico): aprender con un dato a la vez, con ruido, y por qué ese ruido a veces ayuda.
- Momentum y Adam: la versión con memoria e inercia que usan casi todos los entrenamientos reales.
- Mínimos locales, convexidad y por qué en deep learning el paisaje es más complicado (y aun así funciona).
- Regularización (L2 / weight decay): castigar pesos grandes para que el modelo generalice.

## Checkpoint

Lo entendiste si puedes entrenar una regresión lineal solo con descenso de gradiente, sin librerías, y explicar qué pasa si la tasa de aprendizaje es 10x más grande.

> Código en construcción: `descenso_gradiente.py` — gradiente, SGD y Adam sobre la misma función, con gráfica del error bajando.
