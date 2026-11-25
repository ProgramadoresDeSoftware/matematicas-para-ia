# 02 — Cálculo: derivadas y gradiente (cómo aprende un modelo)

## La idea en criollo

La **derivada** es la respuesta a: "si muevo un poquito este número, ¿cuánto cambia el resultado?" Es una pendiente. Si el error baja cuando subo un peso, la derivada me lo dice, y sé hacia dónde moverme.

El **gradiente** es eso mismo, pero para muchos números a la vez: un vector que apunta hacia donde el error crece más rápido. Para bajar el error, caminas en sentido contrario. Eso es entrenar.

## Lo que vas a aprender aquí

- Derivada como pendiente y como "sensibilidad" (regla de la cadena: si A depende de B y B depende de C, el cambio se multiplica en cadena).
- Gradiente, derivadas parciales y jacobiano (la idea, sin formalismo).
- Derivada numérica vs. derivada analítica: cómo verificar que tu gradiente está bien.
- El puente al backprop: la regla de la cadena aplicada a una red entera.

## Checkpoint

Lo entendiste si puedes explicar, sin fórmulas, por qué entrenar es "seguir la pendiente hacia abajo" y qué pasaría si el paso es demasiado grande (te pasas del mínimo) o demasiado chico (tardas una eternidad).

## Código

- [`derivadas_gradiente.py`](derivadas_gradiente.py): derivada numérica vs. analítica, regla de la cadena a mano y descenso de gradiente sobre un cuenco, con tasa de aprendizaje buena (0.1), muy chica (0.01) y muy grande (1.1). Verificado corriendo.
- Notebook en Colab: [Abrir en Colab](https://colab.research.google.com/github/ProgramadoresDeSoftware/matematicas-para-ia/blob/main/02-calculo/derivadas_gradiente.ipynb) — mismo contenido, para resolver los ejercicios y guardar tu copia en Drive.
