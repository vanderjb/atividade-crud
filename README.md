# atividade-crud

CRUD de Funcionários feito com Python, Django e MySQL para a Atividade Avaliativa 2
de Desenvolvimento de Aplicações (Unoesc).

**Aluno:** Vanderlei José Bento Junior

## O que tem no projeto

- `funcionario/` - projeto Django (settings e rotas principais)
- `app/` - app com o model `Funcionario` (nome, cpf, email, remuneracao)
- telas: cadastrar, listar todos, exibir um, editar e remover

Rotas:

| Rota | O que faz |
|---|---|
| `/app/form_funcionario` | cadastrar funcionário |
| `/app/lista_funcionarios` | lista com todos |
| `/app/lista_funcionario/<id>` | exibe os dados de um |
| `/app/form_funcionario/<id>` | editar |
| `/app/remover_funcionario/<id>` | remover |

## Como rodar

1. Criar o banco no MySQL (DBeaver ou Workbench):

   ```sql
   CREATE DATABASE funcionarios;
   ```

2. Criar e ativar a venv e instalar as dependências:

   ```
   virtualenv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Conferir o usuário/senha do MySQL em `funcionario/settings.py`
   (está `root` / `root` na porta 3306).

4. Criar as tabelas e rodar:

   ```
   python manage.py migrate
   python manage.py runserver
   ```

5. Abrir http://localhost:8000/app/lista_funcionarios
