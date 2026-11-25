"""Convierte un .py del repo en un .ipynb para Google Colab.

Uso: python tools/convert_to_notebook.py 02-calculo/derivadas_gradiente.py "02 — Título"

Las lineas '# N. titulo ---...' abren una celda markdown con el titulo y
el codigo que sigue va a una celda de codigo. El bloque final
'# --- Ejercicios ...' se vuelve celda markdown. El docstring inicial
se vuelve la primera celda markdown.
"""
import json
import re
import sys

HEADER = re.compile(r"^# (\d+)\. (.+?)\s*-*\s*$")
EXERCISES = re.compile(r"^# --- Ejercicios")


def convert(py_path, ipynb_path, title):
    with open(py_path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    cells = []
    buf_code = []
    buf_md = []

    def flush_code():
        nonlocal buf_code
        src = "\n".join(buf_code).strip("\n")
        if src.strip():
            cells.append({"cell_type": "code", "execution_count": None,
                          "metadata": {}, "outputs": [],
                          "source": [l + "\n" for l in src.splitlines()]})
        buf_code = []

    def flush_md():
        nonlocal buf_md
        text = "\n".join(buf_md).strip("\n")
        if text.strip():
            cells.append({"cell_type": "markdown", "metadata": {},
                          "source": [l + "\n" for l in text.splitlines()]})
        buf_md = []

    i = 0
    if lines and lines[0].startswith('"""'):
        doc = []
        i = 1
        while i < len(lines) and not lines[i].startswith('"""'):
            doc.append(lines[i])
            i += 1
        i += 1
        cells.append({"cell_type": "markdown", "metadata": {},
                      "source": ["# " + title + "\n", "\n"] +
                      [l + "\n" for l in doc if l.strip()]})

    while i < len(lines):
        line = lines[i]
        m = HEADER.match(line)
        if m:
            flush_code()
            flush_md()
            buf_md = ["## " + m.group(2).strip()]
            i += 1
            continue
        if EXERCISES.match(line):
            flush_code()
            flush_md()
            ex = []
            while i < len(lines):
                ex.append(re.sub(r"^# ?", "", lines[i]))
                i += 1
            ex = [l for l in ex if l.strip() and not re.match(r"^-+\s*$", l.strip())]
            cells.append({"cell_type": "markdown", "metadata": {},
                          "source": ["## Ejercicios\n"] +
                          [l + "\n" for l in ex]})
            break
        if buf_md:
            flush_md()
        buf_code.append(line)
        i += 1
    flush_code()
    flush_md()

    nb = {"cells": cells,
          "metadata": {"kernelspec": {"display_name": "Python 3",
                                       "language": "python",
                                       "name": "python3"},
                       "language_info": {"name": "python", "version": "3.11"}},
          "nbformat": 4, "nbformat_minor": 5}
    with open(ipynb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"{ipynb_path}: {len(cells)} celdas "
          f"({sum(1 for c in cells if c['cell_type'] == 'code')} codigo, "
          f"{sum(1 for c in cells if c['cell_type'] == 'markdown')} texto)")


if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2], sys.argv[3])
