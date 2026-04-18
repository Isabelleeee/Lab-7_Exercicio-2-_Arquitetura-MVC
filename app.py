from flask import Flask, render_template
from models import db_livros

app = Flask(__name__)

# Rota principal (O Controller processa a requisição)
@app.route('/')
def home():
    # 1. Busca os dados no Model
    lista_de_livros = db_livros
    
    # 2. Envia os dados para a View
    return render_template('index.html', livros=lista_de_livros)

if __name__ == '__main__':
    app.run(debug=True)