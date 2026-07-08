import streamlit as st
st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

valor_inicial = st.number_input("Ingrese el valor inicial")
valor_final = st.number_input("Ingrese el valor final")

lista numérica = list(range(valor_inicial, valor_final))
