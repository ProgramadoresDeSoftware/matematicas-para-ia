# 06 — Deep learning: redes neuronales por dentro

## La idea en criollo

Una red neuronal es una cadena de transformaciones simples (matriz + función no lineal, repetidas). Cada capa deforma un poco los datos hasta que el problema se vuelve fácil. Entrenarla es aplicar la regla de la cadena a toda la cadena: eso es **backprop**.

## Lo que vas a aprender aquí

- Funciones de activación (ReLU, sigmoide, tanh): por qué sin ellas la red no aprende nada complejo.
- Backprop a mano, con una red chiquita (2 capas), antes de tocar PyTorch.
- Funciones de pérdida: MSE, cross-entropy y qué mide cada una.
- El mismo MLP en PyTorch, para ver que la librería solo automatiza lo que ya hiciste a mano.
- Inicialización, normalización y por qué a veces el entrenamiento no arranca.

## Checkpoint

Lo entendiste si puedes explicar backprop como "repartir la culpa del error entre los pesos, capa por capa, hacia atrás".

> Código en construcción: `mlp_desde_cero.py` (NumPy) y `mlp_pytorch.py`.
