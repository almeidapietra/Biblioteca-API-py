# Biblioteca API
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/almeidapietra/Biblioteca-API-py/blob/main/LICENSE)

Este projeto é uma API para gerenciar uma biblioteca, desenvolvida como atividade da Residência de Software do GOV BA + CEPEDI. A API permite realizar operações CRUD (Criar, Ler, Atualizar e Excluir) para livros, autores e categorias.

## Tecnologias Utilizadas

- Django
- Django REST Framework

## Estrutura do Projeto

- **core**: Aplicativo principal contendo os modelos, serializadores e views.

## Instruções de Instalação

1. Clone o Repositório:

    ```bash
    git clone https://github.com/almeidapietra/Biblioteca-API-py.git
    ```

2. Instale as Dependências:

    Navegue até o diretório do projeto e instale as dependências usando pip:

    ```bash
    cd nome-do-repositorio
    pip install -r requirements.txt
    ```

3. Configure o Banco de Dados:

    Certifique-se de que o banco de dados SQLite está configurado. O nome do banco de dados está definido como `bib.sqlite3`.

4. Crie as Migrações e Aplique-as:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Inicie o Servidor:

    ```bash
    python manage.py runserver
    ```

    A API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints da API

- **Listar e Criar Livros:**

    - `GET /livros/`
    - `POST /livros/`

- **Detalhes, Atualizar e Excluir Livros:**

    - `GET /livros/<id>/`
    - `PUT /livros/<id>/`
    - `DELETE /livros/<id>/`

## Testes

Para testar a API, você pode usar ferramentas como Postman ou fazer requisições HTTP diretamente no navegador para operações GET.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## contatos:
<div> 
    <a href = "mailto:costapietra@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/almeidapietra" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
</div>
