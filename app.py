from flask import Flask, request, render_template

app = Flask(__name__)

# Liste initiale des livres
books = [
    {'title': 'Le Petit Prince', 'author': 'Antoine de Saint-Exupéry'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'L\'Étranger', 'author': 'Albert Camus'}
]

@app.route('/', methods=['GET'])
def index():
    """Affiche le formulaire pour ajouter un livre et la liste des livres"""
    return render_template("index.html", books=books)

@app.route('/add', methods=["POST"])
def add_book():
    """Ajoute un livre à partir du formulaire"""
    title = request.form.get('title')
    author = request.form.get('author')

    # Vérifier que les champs ne sont pas vides
    if title and author:
        books.append({'title': title, 'author': author})
        return f"Livre ajouté : {title} par {author} <br><a href='/'>Retour</a>"
    else:
        return "Veuillez remplir tous les champs. <br><a href='/'>Retour</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
