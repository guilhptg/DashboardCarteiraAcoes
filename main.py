import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

# criar as funções de carregamento de dados
    # cotação do Itau (ITUB4) - 2010 a 2024


@st.cache_data
def carregar_dados(empresas):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers) # .SA faz referência a bolsa nacional (São Paulo)
    cotacoes_acao = dados_acao.history(period='1d', start='2010-01-01', end='2025-03-01')
    return cotacoes_acao['Close']


@st.cache_data
def carregar_tickers_acoes():
    base_tickers = pd.read_csv('IBOV.csv', sep=';')
    tickers = list(base_tickers['Código'])
    tickers = [item + '.SA' for item in tickers]
    return tickers


# Preparar vizualização

acoes = carregar_tickers_acoes()
# acoes = ['SANB11.SA', 'ITSA4.SA', 'JBSS3.SA', 'SUZB3.SA', 'VIVT3.SA']
dados = carregar_dados(acoes)

st.write("""
# APP Preço de Ações
O gráfico abaixo representa a evolução do preço das ações ao longo do periodo selecionado
""")

# Filtros
st.sidebar.header('Filtros')

# Filtros de ações
lista_acoes = st.sidebar.multiselect("Escolha as ações para vizualizar", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica: 'Close'})
print(lista_acoes)

# Filtro de datas
data_inicial = dados.index.min().to_pydatetime()
data_final = dados.index.max().to_pydatetime()
intervalo_datas = st.sidebar.slider('Selecione o período',
                                    min_value=data_inicial, 
                                    max_value=data_final, 
                                    value=(data_inicial, data_final),
                                    step=timedelta(days=1))
print(intervalo_datas)

dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]


# Criar gráfico
st.line_chart(dados)


#calculo performace
texto_performace_ativos = "Rendimento X"

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={'Close': acao_unica})


# carteira / atribuir um valor variável para carteira
carteira = [1000 for acao in lista_acoes]
total_inicial_carteira = sum(carteira)



for i, acao in enumerate(lista_acoes):
    performace_ativo = dados[acao].iloc[0] / dados[acao].iloc[0] - 1
    performace_ativo = float(performace_ativo)

    carteira[i] = carteira[i] * (1 + performace_ativo)

    if performace_ativo > 0:
        texto_performace_ativos = texto_performace_ativos + f'  \n{acao}: :green[{performace_ativo:.1%}]'

    elif performace_ativo < 0:
        texto_performace_ativos = texto_performace_ativos + f'  \n{acao}: :red[{performace_ativo:.1%}]'

    else:
        texto_performace_ativos = texto_performace_ativos + f'  \n{acao}: :blue[{performace_ativo:.1%}]'

total_final_carteira = sum(carteira)

performace_carteira = total_final_carteira / total_inicial_carteira - 1




if performace_carteira > 0:
    texto_performace_carteira = f'Performace da carteira com todos ativos: :green[{performace_carteira:.2%}]'

elif performace_carteira < 0:
    texto_performace_carteira = f'Performace da carteira com todos ativos: :red[{performace_carteira:.2%}]'

else:
    texto_performace_carteira = f'Performace da carteira com todos ativos: :blue[{performace_carteira:.2%}]'


st.write(f"""
### Performace dos Ativos
Essa foi a performace de cada ativo no período selecionado:

{texto_performace_ativos}

{texto_performace_carteira}

""")
