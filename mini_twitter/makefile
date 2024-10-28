# Nome do projeto Django
PROJECT_NAME=mini_twitter

# Variáveis de ambiente
DJANGO_MANAGE=python manage.py

# Criar o ambiente virtual
venv:
	python -m venv env

# Atualizar dependências
install:
	pip-compile requirements.in
	pip install -r requirements.txt

# Iniciar o servidor 
run:
	$(DJANGO_MANAGE) runserver

# Migrações
migrate:
	$(DJANGO_MANAGE) migrate

# Criar um superusuário
createsuperuser:
	$(DJANGO_MANAGE) createsuperuser

# Abrir o shell do Django
shell:
	$(DJANGO_MANAGE) shell

# Executar testes
test:
	$(DJANGO_MANAGE) test

# Verificar erros de estilo de código com flake8
lint:
	flake8 $(PROJECT_NAME) --exclude=migrations

# Popular o banco de dados com usuários e posts de teste
populate:
	$(DJANGO_MANAGE) shell < scripts/populate_users.py

