"""02 - Calculo: derivada, regla de la cadena, gradiente y descenso.

Corre con:  python 02-calculo/derivadas_gradiente.py
Idea: la derivada dice hacia donde moverte para equivocarte menos.
Entrenar un modelo es seguir esa pendiente hacia abajo, paso a paso.
"""
import numpy as np

# 1. La derivada es una pendiente ---------------------------------------------
# Derivada numerica: mide cuanto cambia f si mueves x un poquito (h).
# Es la pendiente de la curva en ese punto.
def derivada_numerica(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def f(x):
    return x ** 2

print("derivada de x^2 en x=3 (numerica):", derivada_numerica(f, 3.0))  # ~6
print("derivada de x^2 en x=3 (analitica, 2x):", 2 * 3.0)              # 6
# Si la derivada es positiva, la funcion sube; si es negativa, baja;
# si es 0, estas en un minimo, un maximo o un punto plano.

# 2. Regla de la cadena: derivar por dentro y por fuera ------------------------
# h(x) = (2x + 1)^2. Por dentro g(x) = 2x + 1, por fuera F(u) = u^2.
# La regla dice: h'(x) = F'(g(x)) * g'(x) = 2*(2x+1) * 2.
# El cambio se multiplica en cadena: esto es el corazon del backprop.
def h(x):
    return (2 * x + 1) ** 2

def h_prima(x):
    return 2 * (2 * x + 1) * 2

print("h'(1) con la cadena:", h_prima(1.0))                  # 12
print("h'(1) numerica:     ", derivada_numerica(h, 1.0))     # ~12

# 3. Gradiente: la derivada cuando hay varias variables -------------------------
# F(x, y) = (x-3)^2 + (y+1)^2 es un cuenco con el minimo en (3, -1).
# El gradiente es un vector [dF/dx, dF/dy] que apunta hacia donde F
# crece mas rapido. Para bajar, caminas en sentido contrario.
def F(x, y):
    return (x - 3) ** 2 + (y + 1) ** 2

def gradiente(F, x, y, h=1e-5):
    df_dx = (F(x + h, y) - F(x - h, y)) / (2 * h)
    df_dy = (F(x, y + h) - F(x, y - h)) / (2 * h)
    return np.array([df_dx, df_dy])

print("gradiente en (0, 0):  ", gradiente(F, 0.0, 0.0))    # lejos del minimo
print("gradiente en (3, -1): ", gradiente(F, 3.0, -1.0))   # ~[0, 0]: minimo

# 4. Descenso de gradiente: bajar el cuenco paso a paso --------------------------
# Regla: x_nuevo = x - lr * gradiente. lr es la tasa de aprendizaje:
# el tamano del paso. Si es muy grande te pasas del minimo; si es
# muy chica, tardas una eternidad.
def descenso_gradiente(F, x0, lr=0.1, pasos=10):
    x = np.array(x0, dtype=float)
    for i in range(pasos):
        g = gradiente(F, x[0], x[1])
        x = x - lr * g
        print(f"  paso {i + 1}: x={np.round(x, 3)}, error={F(x[0], x[1]):.4f}")
    return x

print("--- lr=0.1 (paso bueno) ---")
descenso_gradiente(F, [0.0, 0.0], lr=0.1, pasos=10)
print("--- lr=0.01 (paso muy chico: casi no avanza) ---")
descenso_gradiente(F, [0.0, 0.0], lr=0.01, pasos=5)
print("--- lr=1.1 (paso muy grande: se pasa y explota) ---")
descenso_gradiente(F, [0.0, 0.0], lr=1.1, pasos=5)

# --- Ejercicios -----------------------------------------------------------------
# 1. Calcula la derivada numerica de g(x) = x^3 en x=2. La analitica es 3x^2.
#    ¿Coinciden? ¿Que pasa si usas h=0.1 en vez de h=1e-5?
# 2. Regla de la cadena: k(x) = (x^2 + 1)^3. Calcula k'(1) a mano con la cadena
#    y verificalo con derivada_numerica. (Pista: por fuera u^3, por dentro x^2+1.)
# 3. Gradiente de G(x, y) = x^2 + y^2 en el punto (1, 2). ¿Hacia donde apunta?
#    ¿Donde esta el minimo de G? Compruebalo con el gradiente en ese punto.
# 4. Con la F de este modulo y lr=0.5, ¿cuantos pasos hacen falta para que el
#    error baje de 0.01? Prueba con lr=0.1 y lr=0.9 y compara.
