# 📚 Livraria MVP - Padrão MVC

Este é o estágio inicial do MVP de uma livraria virtual, desenvolvido para demonstrar a aplicação do padrão de arquitetura **MVC (Model-View-Controller)** em um ambiente web utilizando Python e Flask.

---

## 🏗️ Arquitetura Utilizada

O projeto segue a divisão clássica de responsabilidades do MVC, garantindo que a lógica de dados, a interface e o controle de fluxo estejam separados:

* **Model (`models.py`):** Gerencia os dados e as regras de negócio. Define a estrutura do objeto `Livro` e a simulação do banco de dados.
* **View (`templates/`):** Camada de apresentação que interage com o usuário. Utiliza HTML e a engine **Jinja2** para exibir os dados dinamicamente.
* **Controller (`app.py`):** O cérebro da aplicação. Recebe as requisições do usuário, consulta o Model e decide qual View deve ser renderizada.

---

## 🛠️ Tecnologias

* **Linguagem:** Python 3.x
* **Framework:** Flask
* **Estilização:** CSS3
* **Front-end:** HTML5 + Jinja2

---

## 📂 Estrutura de Pastas

```text
├── app.py             # Controller (Ponto de entrada)
├── models.py          # Model (Estrutura de dados)
├── templates/         # Views (HTML)
│   └── index.html
└── static/            # Assets (CSS/Imagens)
    └── style.css

---

## 🚀 Como Executar

1. Instale o Flask:
   pip install flask

2. Execute o Controller principal:
    python app.py

3. Acesse no navegador:
    http://127.0.0.1:5000
