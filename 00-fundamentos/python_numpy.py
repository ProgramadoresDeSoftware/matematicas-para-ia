"""00 - Fundamentos: funciones, sumatoria, log/exp y NumPy.

Corre con:  python 00-fundamentos/python_numpy.py
Idea: todo en IA es una funcion que transforma numeros.
"""
import numpy as np

# 1. Funciones: entran numeros, salen numeros -------------------------------
def f(x):
    return 2 * x + 1

print("f(3) =", f(3))  # 7

# 2. Sumatoria: un for que suma ----------------------------------------------
x = np.array([1.0, 2.0, 3.0, 4.0])
print("suma =", np.sum(x))            # 10.0  (lo mismo que sum(x))
print("suma de cuadrados =", np.sum(x ** 2))  # 30.0

# 3. Exponencial y logaritmo --------------------------------------------------
print("e^1 =", np.exp(1.0))          # ~2.718
print("log(e) =", np.log(np.exp(1.0)))  # 1.0
# log convierte productos en sumas:
a, b = 100.0, 1000.0
print("log(a*b) =", np.log(a * b), "== log(a)+log(b) =", np.log(a) + np.log(b))

# 4. NumPy: operar sobre miles de numeros de una vez --------------------------
v = np.array([1.0, 2.0, 3.0])
print("v * 2 =", v * 2)               # broadcasting: el 2 se aplica a todo
print("v + v =", v + v)
print("producto punto v.v =", np.dot(v, v))  # 1+4+9 = 14

# Un "modelo" chiquito: y = w*x + b, con w=2, b=1, aplicado a todo el vector
w, b = 2.0, 1.0
print("modelo aplicado a x:", w * x + b)

# --- Ejercicios --------------------------------------------------------------
# 1. Calcula a mano (y luego verifica) np.dot([3, 4], [3, 4]).
# 2. ¿Cuanto vale np.sum(np.log(np.array([10., 100., 1000.])))? ¿Por que?
# 3. Escribe una funcion g(x) = x**2 + 3*x + 1 y aplicala al vector x.
#    ¿Que forma tiene el resultado?
# 4. Cambia w y b del modelo y observa: ¿que cambia en la salida?
