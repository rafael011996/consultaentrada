import pandas as pd
import streamlit as st

# Carregar Excel
@st.cache_data(ttl=0)
def carregar_dados():
    url = 'https://raw.githubusercontent.com/rafael011996/consultaentrada/main/consultaentrada.xlsx'
    return pd.read_excel(url)

# Interface do app
st.title('Consulta de Entradas')

dados = carregar_dados()

# Mostrar somente colunas relevantes
dados = dados[['Nota', 'Emissao', 'Dt.Cont.', 'CGC/CPF', 'Razao', 'Valor da Nota']]

# Entrada de busca
consulta = st.text_input('Digite o Código ou parte da NF:')

if consulta:
    # Filtro de busca
    resultado = dados[dados.apply(lambda row: 
                                  consulta.lower() in str(row['Nota']).lower() or  
                                  consulta.lower() in str(row['Razao']).lower() or                                
                                  consulta.lower() in str(row['CGC/CPF']).lower(), 
                                  axis=1)]
    
    if not resultado.empty:
        st.write('Resultados encontrados:')
        st.dataframe(resultado)
    else:
        st.warning('Nenhum produto encontrado.')
