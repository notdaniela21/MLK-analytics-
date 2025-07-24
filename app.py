import streamlit as st
import matplotlib.pyplot as plt

# Título de la app
st.title('Evaluación de Riesgo Microbiológico en Leche')

# Descripción de la app
st.write("""
    En esta aplicación, puedes ingresar los recuentos de bacterias para evaluar el nivel de riesgo microbiológico.
    Los niveles de riesgo se clasifican en tres categorías:
    - *Bajo*: Recuento bajo de bacterias
    - *Medio*: Recuento medio de bacterias
    - *Alto*: Recuento alto de bacterias
""")

# Entradas del usuario para los recuentos de bacterias
col1e3 = st.number_input('Ingrese el recuento de bacterias para la dilución 10³ (UFC/mL)', min_value=0)
col1e4 = st.number_input('Ingrese el recuento de bacterias para la dilución 10⁴ (UFC/mL)', min_value=0)

# Función para calcular el nivel de riesgo basado en los recuentos
def calcular_riesgo(col1e3, col1e4):
    # Clasificación del riesgo basado en los valores de recuento
    if col1e3 < 100000 and col1e4 < 100000:
        return 'Bajo', 'green'
    elif 100000 <= col1e3 < 500000 or 100000 <= col1e4 < 500000:
        return 'Medio', 'yellow'
    else:
        return 'Alto', 'red'

# Calcular el nivel de riesgo
nivel_riesgo, color = calcular_riesgo(col1e3, col1e4)

# Mostrar el resultado de la evaluación
st.write(f'*Nivel de Riesgo Microbiológico: {nivel_riesgo}*')

# Crear una gráfica de barras que muestre el nivel de riesgo
fig, ax = plt.subplots()

# Bar plot
ax.bar(nivel_riesgo, 1, color=color)
ax.set_ylim(0, 1)
ax.set_title('Nivel de Riesgo Microbiológico')
ax.set_ylabel('Nivel de Riesgo')

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

# Mostrar los recuentos y el nivel de riesgo
st.write(f"Recuento 10³ (UFC/mL): {col1e3}")
st.write(f"Recuento 10⁴ (UFC/mL): {col1e4}")

# Botón para reiniciar los valores (opcional)
if st.button('Reiniciar'):
    st.experimental_rerun()