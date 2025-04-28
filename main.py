import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta

st.set_page_config(layout='wide')

@st.cache_data
def carregar_dados(empresas):
    """
    Carrega os dados históricos de fechamento das ações das empresas especificadas.

    Parâmetros:
    empresas (list of str): Lista de tickers das empresas no formato 'TICKER.SA'.

    Retorna:
    DataFrame: DataFrame contendo os preços de fechamento ajustados das ações.
    """
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers) # .SA faz referência a bolsa nacional (São Paulo)
    cotacoes_acao = dados_acao.history(period='1d', start='2010-01-01', end='2025-03-01')
    return cotacoes_acao['Close']

@st.cache_data
def carregar_tickers_acoes():
    """
    Carrega a lista de tickers das ações do índice IBOV a partir de um arquivo CSV.

    Retorna:
    list of str: Lista de tickers das ações no formato 'TICKER.SA'.
    """
    base_tickers = pd.read_csv('IBOV.csv', sep=';')
    tickers = list(base_tickers['Código'])
    tickers = [item + '.SA' for item in tickers]
    return tickers

# Preparar vizualização

acoes = carregar_tickers_acoes()
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

dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]

# Gráfico de Linha
st.line_chart(dados)

# Cálculo de Performance
texto_performace_ativos = ""

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={'Close': acao_unica})

# Valor Investido no Início do Periodo
valor_investido = st.sidebar.number_input('Valor Investido (R$)', min_value=1.00)

# Carteira / atribuir um valor variável para carteira
carteira = [valor_investido for acao in lista_acoes]
total_inicial_carteira = sum(carteira)

for i, acao in enumerate(lista_acoes):
    performace_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
    performace_ativo = float(performace_ativo)

    carteira[i] = carteira[i] * (1 + performace_ativo)
    print(acao)
    if performace_ativo > 0:
        texto_performace_ativos = texto_performace_ativos + f'  \n{acao}: :green[{performace_ativo:.1%}]'
    elif performace_ativo < 0:
        texto_performace_ativos = texto_performace_ativos + f'  \n{acao}: :red[{performace_ativo:.1%}]'
    else:
        texto_performace_ativos = texto_performace_ativos + f'  \n{acao}: :blue[{performace_ativo:.1%}]'

total_final_carteira = sum(carteira)

performace_carteira = (total_final_carteira / total_inicial_carteira) - 1

total_rendido_reais = valor_investido + (valor_investido * performace_carteira)
cor_total_rendido = ":green" if total_rendido_reais >= 0 else (":red" if total_rendido_reais < 0 else ":blue")

texto_total_rendido_reais = f'### Performance do Investimento  \nTotal: {cor_total_rendido}[R$ {total_rendido_reais:,.2f}]'

if performace_carteira > 0:
    texto_performace_carteira = f'#### Performace da carteira com todos ativos:  \n:green[{performace_carteira:.2%}]'
elif performace_carteira < 0:
    texto_performace_carteira = f'#### Performace da carteira com todos ativos:  \n:red[{performace_carteira:.2%}]'
else:
    texto_performace_carteira = f'#### Performace da carteira com todos ativos:  \n:blue[{performace_carteira:.2%}]'

container = st.container(border=True)
with container:
    st.write(f"""
### Performace dos Ativos
Essa foi a performace de cada ativo no período selecionado:

{texto_performace_ativos}

{texto_performace_carteira}


{texto_total_rendido_reais}

""")
