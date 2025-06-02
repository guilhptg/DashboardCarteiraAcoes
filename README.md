# 📈 Painel Interativo de Ações (Ibovespa)

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b.svg)](https://streamlit.io)
[![yfinance](https://img.shields.io/badge/data%20via-yfinance-yellow)](https://pypi.org/project/yfinance/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> Uma aplicação leve e intuitiva para acompanhar a evolução do preço de ações da bolsa brasileira (B3). Desenvolvida com Python, Streamlit e yFinance.

---

## 🚀 O que essa aplicação faz?

Este painel permite:

- 📊 Visualizar a evolução histórica de preços de ações listadas no **Ibovespa**.
- 🔍 Selecionar múltiplos ativos para comparar em gráficos interativos.
- 📅 Filtrar o período analisado via **slider de datas**.
- 💰 Simular um valor investido e obter a **performance da carteira** no período.
- 🧮 Verificar a **correlação entre os ativos** selecionados.
- ✅ Tudo isso direto do navegador, com interface simples e sem complicações.

---

## 🖼️ Exemplo de uso

> O usuário seleciona PETR4.SA, ITUB4.SA e VALE3.SA, escolhe o intervalo entre 2020 e 2024, simula um investimento de R$ 10.000 e vê:

- A evolução dos preços no tempo
- Correlação entre os ativos
- Retorno percentual individual e da carteira como um todo
- Valor final investido

---

## 🧰 Tecnologias utilizadas

- **Python 3.12+**
- [Streamlit](https://streamlit.io/) — Web app interativo
- [yFinance](https://pypi.org/project/yfinance/) — Para puxar os dados históricos das ações
- **Pandas**, **datetime**, **Altair** (por trás do Streamlit)

---

## 🐳 Como rodar com Docker (opcional)

> ⚠️ Docker é opcional, mas garante ambiente padronizado e sem erros de dependência.

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo

# Build da imagem
docker build -t painel-acoes .

# Execute
docker run -p 8501:8501 painel-acoes
```

Abra no navegador:
🔗 http://localhost:8501

💻 Como rodar localmente (sem Docker)
Pré-requisitos: Python 3.12+ e pip.

```bash
# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS

# .venv\Scripts\activate    # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação

streamlit run main.py
```
# 📁 Estrutura do projeto
```arduino
.
├── IBOV.csv              # Lista dos tickers das ações do Ibovespa
├── main.py               # Código principal do aplicativo
├── requirements.txt      # Dependências do projeto
├── Dockerfile            # (Opcional) Imagem Docker para build
├── README.md             # Este arquivo
└── .streamlit/
    └── config.toml       # Configurações visuais do Streamlit
```
# 📝 Como funciona?
- IBOV.csv: lista com os códigos das ações (ex: PETR4) usada para popular o menu lateral.

- yFinance: coleta os preços de fechamento ajustados para os ativos selecionados.

- Streamlit: exibe gráfico de linha com os preços e calcula a performance de cada ativo e da carteira como um todo.

- Simulador de investimento: insira um valor e veja o quanto teria rendido!

# 🧠 Detalhes técnicos
- Cálculo de performance com base na variação percentual entre o primeiro e o último valor do período selecionado.

- Carteira simulada considera alocação igual entre ativos.

- Exibição de resultados com cores que refletem o retorno:

    - 🟩 Verde para ganhos

    - 🟥 Vermelho para perdas

    - 🔵 Azul para neutro

# 📜 Licença
Distribuído sob a licença MIT. Veja [[License]](LICENSE)
 para mais informações.

# ☕ Contribuições & Feedback
Ideias, bugs ou melhorias?
Fique à vontade para abrir uma issue ou enviar um PR!
Feito com 💙 por Guilherme Portugal.

# 📫 Contato 
Guilherme Portugal

🔗 [LinkedIn](https://www.linkedin.com/in/guilhptg) \
🐙 [GitHub](https://github.com/guilhptg) \
📧 [Email](guilherme.portugal.busi@gmail.com)

