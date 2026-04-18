# 📚 Livraria MVP - Padrão MVC

Este é o estágio inicial do MVP de uma livraria virtual, desenvolvido para demonstrar a aplicação do padrão de arquitetura **MVC (Model-View-Controller)** em um ambiente web utilizando Python e Flask.

---

## 🏗️ Arquitetura Utilizada

O projeto segue a divisão clássica de responsabilidades do MVC, garantindo que a lógica de dados, a interface e o controle de fluxo estejam separados:

* **Model (`models.py`):** Gerencia os dados e as regras de negócio. Define a estrutura do objeto `Livro` e a simulação do banco de dados na memória.
* **View (`templates/`):** Camada de apresentação que interage com o usuário. Utiliza HTML e a engine **Jinja2** para exibir os dados dinamicamente.
* **Controller (`app.py`):** O cérebro da aplicação. Recebe as requisições HTTP, consulta o Model e decide qual View deve ser renderizada.

---

## 🛠️ Tecnologias

* **Linguagem:** Python 3.x
* **Framework:** Flask
* **Front-end:** HTML5 + CSS3 + Jinja2
* **Versionamento:** Git

---

## 📂 Estrutura de Pastas

```text
├── app.py             # Controller (Ponto de entrada)
├── models.py          # Model (Estrutura de dados)
├── templates/         # Views (HTML)
│   └── index.html
└── static/            # Assets (Estilização)
    └── style.css
```

---

## 🚀 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repo.git](https://github.com/seu-usuario/nome-do-repo.git)
   ```

2. **Instale as dependências:**
   ```bash
   pip install flask
   ```

3. **Inicie a aplicação:**
   ```bash
   python app.py
   ```

4. **Acesse no navegador:**
   Abra `http://127.0.0.1:5000` para visualizar o front-end funcionando.
