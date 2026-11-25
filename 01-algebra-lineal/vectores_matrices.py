"""01 - Algebra lineal: vectores, producto punto, matrices y parecido.

Corre con:  python 01-algebra-lineal/vectores_matrices.py
"""
import numpy as np

# 1. Vectores y su largo (norma) ----------------------------------------------
a = np.array([3.0, 4.0])
print("norma de [3,4] =", np.linalg.norm(a))  # 5.0

# 2. Producto punto = parecido -------------------------------------------------
# "gato" y "perro" deberian parecerse mas entre si que con "auto".
gato = np.array([0.9, 0.1, 0.8])
perro = np.array([0.8, 0.2, 0.7])
auto = np.array([0.1, 0.9, 0.1])
print("gato.perro =", np.dot(gato, perro))  # grande: parecidos
print("gato.auto  =", np.dot(gato, auto))   # chico: distintos

def similitud_coseno(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

print("cos(gato, perro) =", similitud_coseno(gato, perro))
print("cos(gato, auto)  =", similitud_coseno(gato, auto))

# 3. Matriz = transformacion ----------------------------------------------------
# Una capa de red neuronal: y = M @ x + b
M = np.array([[2.0, 0.0],
              [0.0, 0.5]])  # estira x al doble, encoge y a la mitad
x = np.array([1.0, 2.0])
print("M @ x =", M @ x)  # [2., 1.]

# 4. Resolver un sistema: M @ x = b  ->  x = ? ---------------------------------
b = np.array([4.0, 1.0])
print("x que resuelve M @ x = b:", np.linalg.solve(M, b))

# 5. Determinante: cuanto estira/encoge -----------------------------------------
print("det(M) =", np.linalg.det(M))  # 1.0: estira un lado y encoge el otro

# --- Ejercicios -----------------------------------------------------------------
# 1. Inventa 3 vectores de 3 numeros: dos parecidos y uno distinto.
#    Verifica con similitud_coseno que tu intuicion era correcta.
# 2. Cambia M por una matriz de rotacion [[0,-1],[1,0]] y aplica M @ [1,0].
#    ¿A donde apunta el vector ahora? Dibujalo.
# 3. ¿Que pasa con np.linalg.solve si M = [[1,2],[2,4]]? ¿Por que?
#    (Pista: mira su determinante.)
# 4. Reto: con vectores de 4 numeros, representa "rey", "reina", "hombre",
#    "mujer" y verifica que rey - hombre + mujer se parezca a reina.
#    Esa es la analogia famosa de los embeddings (word2vec).
