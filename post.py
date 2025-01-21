from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def search():
    nom=request.form.get['username']
    return f"Nom {nom}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80))