# Informa a imagem base
FROM python:3.9
# Define o variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Diretorio do projeto
WORKDIR /app
# Copia o arquivo de dependências do projeto para o diretório
COPY requirements.txt /app/
# Instala as dependências do arquivo
RUN pip install --no-cache-dir -r requirements.txt
# Copia os arquivos da raiz para o diretório
COPY . /app/ 
# Expõe a porta 8000 
EXPOSE 8000
# Comando para rodar o projeto 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
