# Usa a imagem oficial do Python
FROM python:3.12

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para dentro do contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pelo Streamlit
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
