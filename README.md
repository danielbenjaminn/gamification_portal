# Portal de Campanhas de Gamificação

## Objetivo
Desenvolver um portal de campanhas de gamificação onde administradores podem gerenciar campanhas e corretores podem participar dos desafios.

## Requisitos Básicos

### Administradores
- **Cadastrar Desafios:** Incluir nome do desafio, descrição detalhada do desafio, identidade visual (banner), e regras de pontuação (por exemplo, a cada R$600 em vendas na categoria Vida, acumula 1 ponto). Você pode incluir mais campos, se achar necessário.
- **Gerenciar Usuários:** Cadastrar, editar, excluir e visualizar corretores e outros administradores.
- **Atribuir Desafios:** Atribuir desafios a corretores específicos através do CPF.

### Corretores
- **Visualizar Desafios Atribuídos:** Acessar uma lista de desafios que foram especificamente atribuídos a eles.
- **Aceitar Participar de Desafios:** Opção de opt-in para participar em desafios após visualizar detalhes completos incluindo regras e potenciais recompensas.
- **Visualizar Detalhes dos Desafios:** Incluir identidade visual, descrição completa e regras do desafio.

## Requisitos Diferenciais
- Implementação de um sistema de ranking para corretores, incluindo visualização de posição nos desafios.
- Qualidade nos commits para entendermos sua linha de raciocínio.
- Uso de banco de dados relacional, como PostgreSQL ou MySQL.

## Status do Projeto
Atualmente, o projeto ainda não está totalmente pronto. Os seguintes ajustes precisam ser feitos:
- Ajustar o opt-in para aceitar participar do Desafio;
- Melhorar a visualização dos detalhes do desafio;
- Melhorar os templates.

## Configuração do Ambiente

### Pré-requisitos
- Python 3.11
- Django 5.0.7
- MySQL 8.0

### Instalação

1. Clone o repositório:
    ```bash
    git clone 
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados no arquivo `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome_do_banco_de_dados',
            'USER': 'usuario',
            'PASSWORD': 'senha',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. Execute as migrações:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```