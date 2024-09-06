from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():

    livros = [
        {'titulo': 'Coraline', 'paginas': 224},
        {'titulo': 'O Mundo de Sobras (O nascimento do vampiro)', 'paginas': 351},
        {'titulo': 'O Conto da Aia', 'paginas': 366}
    ]
    return render_template('index.html', livros=livros)

if __name__ == "__main__":
    app.run(debug=True)