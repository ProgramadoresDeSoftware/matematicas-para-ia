# 07 — Transformers y agentes: cómo funciona un LLM por dentro

## La idea en criollo

Un transformer no lee una frase palabra por palabra: cada palabra mira a todas las demás y decide a cuál prestarle atención. Esa decisión es matemática pura: producto punto entre vectores (módulo 01), softmax (módulo 03) y muchas capas (módulo 06).

## Lo que vas a aprender aquí

- **Atención**: `softmax(QK^T / sqrt(d_k)) V`, pieza por pieza, en criollo y con código.
- Embeddings posicionales: cómo sabe el modelo en qué orden van las palabras.
- Por qué escalar por `sqrt(d_k)` y qué pasa si no lo haces.
- Fine-tuning y **LoRA**: la idea matemática de entrenar barato (actualizar una matriz grande con dos chiquitas).
- Conexión con tu especialización: cómo un agente LangGraph usa todo esto por debajo (estado, herramientas, memoria) sin que tengas que re-derivar nada, pero entendiéndolo.

## Checkpoint

Lo entendiste si puedes calcular la atención a mano con 3 palabras y vectores de 2 números, y explicar por qué una palabra le presta más atención a otra.

> Código en construcción: `atencion_a_mano.py` — atención con NumPy, sin librerías.
> Proyecto de cierre del repo: un mini-transformer o un clasificador con embeddings entrenados por ti, y una página en el README contando qué aprendiste.
