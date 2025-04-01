from flask import Flask
from flask_cors import CORS
from server.routes.search import search_bp

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Registrar o blueprint
app.register_blueprint(search_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)