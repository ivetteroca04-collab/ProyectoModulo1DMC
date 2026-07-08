import streamlit as st

st.title("Proyecto módulo 1 Fundamentals")
st.sidebar.title("Parámetros")

valor_inicial = st.number_input("Ingrese el valor inicial")
valor_final = st.number_input("Ingrese el valor final")

lista_numerica = list(range(int(valor_inicial), int(valor_final)))

st.write(lista_numerica)
