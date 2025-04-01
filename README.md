# API Test - Busca de Operadoras

Este projeto é uma aplicação web que permite realizar buscas em um arquivo CSV contendo informações sobre operadoras. Ele utiliza Flask no backend e Vue.js no frontend.

---

## 📋 Funcionalidades

- Busca de operadoras com base em um termo de pesquisa.
- Exibição de resultados em uma tabela responsiva.
- Mensagem amigável quando nenhum resultado é encontrado.

---

## 🛠️ Tecnologias Utilizadas

### Backend:
- **Python** (Flask)
- Manipulação de dados com **Pandas**

### Frontend:
- **Vue.js** (Componentização e reatividade)
- Estilização com **CSS**

---

## 📂 Estrutura do Projeto

```plaintext
api-test/
├── server/
│   ├── routes/
│   │   └── search.py         # Rota de busca no backend
│   ├── services/
│   │   └── search_service.py # Lógica de busca no DataFrame
│   ├── utils/
│   │   └── csv_loader.py     # Função para carregar o CSV
│   └── app.py                # Arquivo principal do servidor Flask
├── web/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.vue     # Componente da barra de busca
│   │   │   ├── ResultsTable.vue # Componente da tabela de resultados
│   │   │   └── SearchComponent.vue # Componente principal
│   │   └── App.vue              # Componente raiz do Vue.js
│   └── public/
│       └── index.html           # HTML principal
├── postman/
│   └── api-test.postman_collection.json # Coleção do Postman para testar as APIs
└── [README.md]                  
````

---

## 🧪 Testando a API com Postman

1. Importe a coleção do Postman localizada em `postman/api-test.postman_collection.json`.
2. Certifique-se de que o backend está rodando em `http://127.0.0.1:5000`.
3. Use o Postman para enviar requisições para as rotas da API, como `/search`.

### Exemplo de Requisição:
- **Rota**: `GET /search`
- **Parâmetro**: `q` (termo de busca)
- **Exemplo**: `http://127.0.0.1:5000/search?q=operadora`

## Como rodar o projeto:

### Api Python:

1. Instale as dependencias do Python
    ``` bash
    pip install -r requirements.txt

2. Navegue até o diretorio do servidor:
    ``` bash
    cd server

3. Inicie o servidor Flask:
    ```bash
    flask run


### Frontend Vue:

1. Navegue até o diretório do fron
    ``` bash
    cd ..
    cd web

2. Instale as dependencias do projeto:
    ``` bash
    npm install

3. Execute o servidor de Desenvolvimento:
    ``` bash
    npm run serve
