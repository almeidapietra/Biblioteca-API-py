# Biblioteca API

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/almeidapietra/Biblioteca-API-py/blob/main/LICENSE)

Este projeto é uma API para gerenciar uma biblioteca, desenvolvida como atividade da Residência de Software do GOV BA + CEPEDI. A API permite realizar operações CRUD (Criar, Ler, Atualizar e Excluir) para livros, autores, categorias e coleções personalizadas de livros associadas a usuários autenticados.

## Tecnologias Utilizadas

- Django
- Django REST Framework
- drf-spectacular
- django-cors-headers
- coverage.py

## Estrutura do Projeto

- `core`: Aplicativo principal contendo os modelos, serializadores e views.
- `custom_permissions.py`: Arquivo que define permissões personalizadas para as coleções.

## Novas Funcionalidades

### Exposição Virtual de Coleções de Livros
Agora, os usuários podem criar e gerenciar suas próprias coleções de livros, compartilhando suas obras favoritas de forma organizada. Apenas o colecionador (usuário que criou a coleção) pode editá-la ou excluí-la, mas outros usuários podem visualizar e listar coleções.

### Autenticação e Permissões
- Autenticação baseada em Token foi implementada para proteger os recursos.
- Apenas usuários autenticados podem criar, editar ou excluir coleções.
- Permissões personalizadas garantem que apenas o colecionador possa modificar suas coleções.

### Documentação da API
A API está documentada utilizando **drf-spectacular**, permitindo fácil visualização dos endpoints e seus usos.

### Suporte a CORS
Configuração de **django-cors-headers** para permitir que clientes externos consumam a API, com suporte específico para o IP `192.168.1.100`.

## Passos para Configuração

1. Clone o Repositório:
    ```bash
    git clone https://github.com/almeidapietra/Biblioteca-API-py.git
    ```

2. Instale as Dependências:
    ```bash
    cd Biblioteca-API-py
    pip install -r requirements.txt
    ```

3. Configure o Banco de Dados:
    Certifique-se de que o banco de dados SQLite está configurado. O nome do banco de dados está definido como `bib.sqlite3`.

4. Crie as Migrações e Aplique-as:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Configure as Variáveis de Ambiente (se necessário) para a autenticação e CORS.

6. Inicie o Servidor:
    ```bash
    python manage.py runserver
    ```
    A API estará disponível em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Endpoints da API

### Livros
- **Listar e Criar Livros**:
  - GET `/livros/`
  - POST `/livros/`
- **Detalhes, Atualizar e Excluir Livros**:
  - GET `/livros/<id>/`
  - PUT `/livros/<id>/`
  - DELETE `/livros/<id>/`

### Coleções
- **Listar e Criar Coleções**:
  - GET `/colecoes/`
  - POST `/colecoes/`
- **Detalhes, Atualizar e Excluir Coleções**:
  - GET `/colecoes/<id>/`
  - PUT `/colecoes/<id>/`
  - DELETE `/colecoes/<id>/`

Documentação completa disponível no endpoint `/schema/` e na interface `/docs/` gerada por **drf-spectacular**.

## Testes

### Desenvolvimento de Testes Automatizados
Os testes verificam:
- Criação de coleções associadas ao colecionador.
- Permissões de acesso (edição e exclusão permitidas apenas ao colecionador).
- Restrição para usuários não autenticados.
- Listagem de coleções visíveis para outros usuários autenticados.

### Cobertura de Testes
Use o `coverage.py` para verificar a cobertura de código:
```bash
coverage run manage.py test
coverage report
coverage html
```

Nota: A pasta htmlcov está versionada no repositório apenas para facilitar a correção.


## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## contatos:
<div> 
    <a href = "mailto:costapietra@gmail.com"><img loading="lazy" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="https://www.linkedin.com/in/almeidapietra" target="_blank"><img loading="lazy" src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
</div>
