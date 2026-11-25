# 03 — Probabilidad y estadística: el azar con reglas

## La idea en criollo

Un modelo no dice "esto es así". Dice: **"de todo lo que podría pasar, esto es lo más probable"**. La probabilidad es el idioma en el que hablan los modelos: clasificar, predecir la siguiente palabra, estimar riesgo, todo es probabilidad.

## Lo que vas a aprender aquí

- Probabilidad condicional y **teorema de Bayes**: cómo cambia tu opinión cuando llega evidencia nueva. Es el corazón de un clasificador.
- Distribuciones: normal, Bernoulli, categórica. Qué forma tiene el azar en cada caso.
- Esperanza y varianza: el valor típico y cuánto se dispersan los datos.
- **MLE (máxima verosimilitud)**: entrenar es elegir los parámetros que hacen más probables los datos que viste.
- Entropía y divergencia KL: cómo medir sorpresa y diferencia entre dos distribuciones. Aquí nace el loss de un LLM.

## Checkpoint

Lo entendiste si puedes explicar por qué un modelo de lenguaje es, en el fondo, una máquina de calcular "¿qué palabra viene ahora, con qué probabilidad?".

> Código en construcción: `bayes_y_distribuciones.py` — Bayes a mano, una distribución normal simulada y entropía de una moneda cargada.
