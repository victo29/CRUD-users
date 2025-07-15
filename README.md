# CRUD-users (FastAPI + Clean Architecture)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-0ba360?logo=fastapi)

Este é um projeto de API REST para gerenciamento de usuários, com as operações de **Create**, **Read**, **Update** e **Delete (CRUD)**. Ele foi desenvolvido com **Python**, utilizando o framework **FastAPI**, e segue os princípios da **Clean Architecture**.

O projeto foi baseado no curso gratuito do canal **Programador Lhama** no YouTube:
📺 [Clean Architecture em Python - Programador Lhama](https://www.youtube.com/watch?v=2nvbgwFE_0Y&list=PLAgbpJQADBGK0opZ8ZuDX3zDjQck_QKMy)

---

## 🛠 Tecnologias utilizadas

- **Python**
- **FastAPI**
- **Pydantic**
- **Docker**
- **SQLAlchemy**
- **Uvicorn**
- **Clean Architecture**

---

## 🚀 Modificações realizadas

Este projeto é uma versão adaptada do original feito com **Flask**. Aqui estão as principais modificações feitas:

- 🔁 **Substituição do Flask por FastAPI**
- 🔐 **Uso do Pydantic**
- ➕ **Criação de novas rotas** que não estavam no projeto original:
  - `GET /users/listUsers`
  - `PUT /users/update?id=`
  - `DELETE /users/delete?id=`

💡 **Ponto positivo:** A migração para FastAPI, aliada ao uso de Pydantic, melhora a legibilidade do código, a performance da API e facilita a manutenção e expansão do projeto.

---

## 📌 Rotas disponíveis

| Método | Rota                         | Descrição                         |
|--------|------------------------------|-----------------------------------|
| POST   | `/users/register`           | Registra um novo usuário          |
| GET    | `/users/find?first_name=`   | Busca um usuário pelo primeiro nome |
| GET    | `/users/listUsers`          | Lista todos os usuários           |
| PUT    | `/users/update?id=`         | Atualiza os dados de um usuário   |
| DELETE | `/users/delete?id=`         | Remove um usuário pelo ID         |

---

## 📦 Exemplo de Body (JSON)

As rotas **POST /users/register** e **PUT /users/update** exigem o seguinte corpo:

```json
{
  "first_name": "string",
  "last_name": "string",
  "age": 0
}
```

---

## 🐳 Como executar com Docker

1. Clone este repositório:
   ```bash
   git clone https://github.com/victo29/CRUD-users.git
   cd CRUD-users
   ```

3. Crie o arquivo .env
   ```bash
   DB_USER=clean_db_user
   DB_PASSWORD=root
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=clean_db
   ```

3. Construa e execute o container:
   ```bash
   docker-compose up --build
   ```



4. Acesse a documentação interativa da API:
   ```
   http://localhost:8000/docs
   ```



## 🧠 Aprendizados

- Estruturação de projeto com Clean Architecture
- Uso de FastAPI para criação de APIs modernas e eficientes
- Validação com Pydantic
- Dockerização de aplicações Python
- Criação e manipulação de rotas RESTful

---

## 📌 Progresso do Projeto

| Etapa      | Descrição                                                            | Status       |
|------------|----------------------------------------------------------------------|--------------|
| ✅ Etapa 1 | Construção da API Backend com FastAPI + Clean Architecture           | Concluída    |
| 🛠️ Etapa 2 | Desenvolvimento do Frontend com React + TypeScript + Material UI                 | Em breve  |
