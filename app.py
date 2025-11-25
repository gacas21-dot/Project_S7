import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
data = pd.read_csv('vehicles_us.csv')

# Crear una aplicación simple con Streamlit
st.header("🚗 Vehicle Data Dashboard")

# Información básica
st.write(f"Total de vehículos: {len(data):,}")
st.write(f"Precio promedio: ${data['price'].mean():,.0f}")

hist_button = st.button("Show Vehicle Data")

# Ejecutar el primer botón para mostrar los datos en un histograma
if hist_button:
    st.write('### Distribución de Precios de Vehículos')

    # CHistograma de precios
    fig = go.Figure(data=[go.Histogram(x=data['price'])])
    fig.update_layout(title='Distribución de Precios',
                      xaxis_title='Precio ($)',
                      yaxis_title='Cantidad')
    st.plotly_chart(fig, use_container_width=True)

# Ejecutar el segundo botón para mostrar el gráfico de dispersión
scatter_button = st.button("Show Scatter Plot")
if scatter_button:
    st.write('### Relación entre Odómetro y Precio')

    # Crear un gráfico de dispersión entre odómetro y precio
    fig = go.Figure(
        data=[go.Scatter(x=data['odometer'], y=data['price'], mode='markers')])
    fig.update_layout(title_text='Relación entre Odómetro y Precio',
                      xaxis_title='Odómetro',
                      yaxis_title='Precio ($)')
    st.plotly_chart(fig, use_container_width=True)

    # Agregar correlación
    correlation = data['price'].corr(data['odometer'])
    st.write(f"Correlación: {correlation:.3f}")

# Top 10 marcas
brands_button = st.button("Show Top 10 Models")
if brands_button:
    st.write('### 🏆 Top 10 Modelos Más Populares')

    # Obtener las 10 marcas más populares
    top_brands = data['model'].value_counts().head(10)
    # Crear gráfico de barras
    fig = go.Figure(data=[go.Bar(x=top_brands.index, y=top_brands.values)])
    fig.update_layout(title='Top 10 Modelos',
                      xaxis_title='Modelo',
                      yaxis_title='Cantidad de Vehículos')
    st.plotly_chart(fig, use_container_width=True)
