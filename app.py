import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Funciones Cuadráticas", layout="centered")

st.title("🧠 Simulador Educativo de Funciones Cuadráticas")

# Sliders para los coeficientes
a = st.slider("Coeficiente a (abre hacia arriba o abajo)", -10.0, 10.0, 1.0, 0.5)
b = st.slider("Coeficiente b (desplaza el vértice en X)", -10.0, 10.0, 0.0, 0.5)
c = st.slider("Coeficiente c (intersección con el eje Y)", -10.0, 10.0, 0.0, 0.5)

# Generación de puntos
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

# Graficar la parábola
fig, ax = plt.subplots()
ax.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Retroalimentación automática
st.subheader("📌 Retroalimentación sobre la parábola")

if a > 0:
    st.write("✔️ La parábola abre hacia **arriba** porque el coeficiente **a** es positivo.")
elif a < 0:
    st.write("✔️ La parábola abre hacia **abajo** porque el coeficiente **a** es negativo.")
else:
    st.write("⚠️ Esto no es una parábola (a = 0), es una línea recta.")

if b == 0:
    st.write("📍 La parábola es simétrica respecto al eje **Y** porque **b = 0**.")

if c == 0:
    st.write("📍 La parábola pasa por el **origen (0,0)** porque **c = 0**.")

# Vértice
xv = -b / (2 * a) if a != 0 else 0
yv = a * xv**2 + b * xv + c if a != 0 else 0
st.write(f"📈 El vértice está en el punto **({xv:.2f}, {yv:.2f})**.")
