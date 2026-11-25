# Matemáticas para IA — de cero a modelos

> Aprender la matemática que de verdad usan los modelos de IA, de menos a más, en criollo y con código que corre. Sin tutorial-hell: cada módulo cierra con algo que tú mismo programaste.

## Para quién es esto

Para un backend que ya programa, sabe Python básico y quiere entender **por qué** funciona un modelo, no solo llamar a una API. Si una fórmula te suena a chino, aquí se explica primero en palabras, luego con un ejemplo chiquito, y al final con código.

## La ruta (de menos a más)

| Módulo | Tema | Pregunta que responde | Al terminar sabes hacer |
|---|---|---|---|
| [00 — Fundamentos](00-fundamentos/) | Repaso + Python numérico | ¿Qué necesito tener fresco antes de empezar? | Funciones, sumatorias, log/exp y NumPy sin miedo |
| [01 — Álgebra lineal](01-algebra-lineal/) | Vectores y matrices | ¿Cómo "piensa" un modelo con números? | Embeddings, similitud, sistemas lineales |
| [02 — Cálculo](02-calculo/) | Derivadas y gradiente | ¿Cómo aprende un modelo de sus errores? | Regla de la cadena, gradiente, backprop (la idea) |
| [03 — Probabilidad y estadística](03-probabilidad-estadistica/) | Azar con reglas | ¿Cómo decide un modelo entre opciones? | Bayes, distribuciones, entropía, MLE |
| [04 — Optimización](04-optimizacion/) | Bajar el error | ¿Cómo encuentra el modelo los mejores pesos? | Descenso de gradiente, SGD, Adam |
| [05 — ML desde cero](05-machine-learning-desde-cero/) | Modelos con NumPy | ¿Puedo construir un modelo sin librerías mágicas? | Regresión lineal/logística, k-means, PCA |
| [06 — Deep learning](06-deep-learning/) | Redes neuronales | ¿Qué es entrenar una red, por dentro? | Backprop a mano, MLP, PyTorch |
| [07 — Transformers y agentes](07-transformers-y-agentes/) | Atención y LLMs | ¿Cómo funciona ChatGPT por dentro? | Atención, softmax, embeddings, LoRA (la idea) |

## Reglas del repo

1. **Primero en criollo, luego la fórmula, luego el código.** Nunca al revés.
2. **Nada de copiar-pegar sin entender.** Cada archivo `.py` se corre con `python archivo.py` y tiene ejercicios al final.
3. **Un módulo no se da por terminado hasta que el código corre y el ejercicio está resuelto.** Esa es la regla anti-abandono.
4. **5 horas por semana, en bloques de 2h + 2h + 1h.** Un módulo ≈ 1 semana. Sin apuro: 8 módulos ≈ 8 semanas.

## Cómo empezar

**En la nube, sin instalar nada (recomendado):** abre los notebooks directo en Google Colab con tu cuenta de Google. Ahí corren, y con *Archivo → Guardar una copia en Drive* tus prácticas quedan guardadas en tu Drive.

- Módulo 00: [Abrir en Colab](https://colab.research.google.com/github/ProgramadoresDeSoftware/matematicas-para-ia/blob/main/00-fundamentos/python_numpy.ipynb)
- Módulo 01: [Abrir en Colab](https://colab.research.google.com/github/ProgramadoresDeSoftware/matematicas-para-ia/blob/main/01-algebra-lineal/vectores_matrices.ipynb)

**En tu computadora:**

```bash
git clone https://github.com/ProgramadoresDeSoftware/matematicas-para-ia.git
cd matematicas-para-ia
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python 00-fundamentos/python_numpy.py
```

Luego sigue en orden: lee el `README.md` de cada módulo y corre su código.

## Mapa mental (la idea en una frase por módulo)

- **Álgebra lineal:** los datos son vectores; un modelo es una matriz que los transforma.
- **Cálculo:** la derivada dice hacia dónde moverte para equivocarte menos.
- **Probabilidad:** un modelo no dice "esto es así", dice "esto es lo más probable".
- **Optimización:** entrenar es bajar una montaña (el error) a pasitos, con los ojos vendados, siguiendo la pendiente.
- **Deep learning:** muchas transformaciones simples, encadenadas, aprenden cosas complejas.
- **Transformers:** la atención es una forma matemática de decidir "a qué parte de la frase le presto atención".

## Recursos que se usan (gratis)

- NumPy para todo lo numérico. PyTorch solo aparece en el módulo 06, cuando ya entiendes lo que hace por dentro.
- 3Blue1Brown (YouTube, serie *Essence of Linear Algebra* y *Essence of Calculus*) para verlo en movimiento.
- Platzi: el plan de especialización en IA corre en paralelo a este repo; aquí está la matemática que esos cursos dan por sentada.

## Progreso

- [ ] 00 — Fundamentos
- [ ] 01 — Álgebra lineal
- [ ] 02 — Cálculo
- [ ] 03 — Probabilidad y estadística
- [ ] 04 — Optimización
- [ ] 05 — ML desde cero
- [ ] 06 — Deep learning
- [ ] 07 — Transformers y agentes

Marca cada casilla solo cuando el código del módulo corre y resolviste sus ejercicios.
