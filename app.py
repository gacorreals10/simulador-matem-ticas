# -------------------------------
# app.py - Simulador Matemático
# -------------------------------

# Importamos las librerías necesarias
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la app
st.title("Simulador Interactivo - Funciones Cuadráticas")

# Subtítulo
st.subheader("Explora cómo cambia la gráfica de una parábola")

# Explicación al usuario
st.markdown("Modifica los valores de a, b y c para visualizar la función cuadrática: **y = ax² + bx + c**")

# Slider para modificar los coeficientes
a = st.slider("Coeficiente a", -10.0, 10.0, 1.0)
b = st.slider("Coeficiente b", -10.0, 10.0, 0.0)
c = st.slider("Coeficiente c", -10.0, 10.0, 0.0)

# Dominio de x
x = np.linspace(-10, 10, 400)

# Ecuación cuadrática
y = a * x**2 + b * x + c

# Mostrar la gráfica
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True)
ax.legend()
st.pyplot(fig)
