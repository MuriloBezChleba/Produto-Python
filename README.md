# Produto-Python

Este projeto é uma aplicação simples que interage com um banco de dados MySQL para armazenar e atualizar informações sobre produtos, como nome e preço. Através da interface gráfica do Tkinter, o usuário pode realizar operações básicas de **CRUD** (Criar, Ler, Atualizar e Deletar) para gerenciar produtos.

## Funcionalidades

- **Criar Produto**: Adiciona um novo produto ao banco de dados.
- **Ler Produtos**: Exibe todos os produtos armazenados no banco de dados.
- **Deletar Produto**: Remove um produto existente do banco de dados.
- **Atualizar Produto**: Permite atualizar o nome ou o valor de um produto específico.

## Requisitos

### Software

- **Python 3.x**: A aplicação é desenvolvida utilizando Python.
- **MySQL**: Requer um banco de dados MySQL para armazenar as informações dos produtos.

### Bibliotecas Python

Este projeto usa a biblioteca **mysql-connector-python** para interagir com o banco de dados MySQL. Para instalá-la, utilize o seguinte comando:

```bash
pip install mysql-connector-python
