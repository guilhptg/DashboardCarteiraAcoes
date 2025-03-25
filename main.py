import streamlit as st
import pandas as pd
import yfinance as yf

# criar as funções de carregamento de dados
    # cotação do Itau (ITUB4) - 2010 a 2024


@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers) # .SA faz referência a bolsa nacional (São Paulo)
    cotacoes_acao = dados_acao.history(period='1d', start='2010-01-01', end='2025-03-01')
    return cotacoes_acao['Close']

# Preparar vizualização

acoes = ['ITUB4.SA', 'PETR4.SA', 'MGLU3.SA', 'VALE3.SA', 'ABEV3.SA', 'GGBR4.SA']
dados = carregar_dados(acoes)

st.write("""
# APP Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo do periodo selecionado
""")

# Filtros
lista_acoes = st.multiselect("Escolha as ações para vizualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: 'Close'})

print(lista_acoes)






# Criar gráfico
st.line_chart(dados)

