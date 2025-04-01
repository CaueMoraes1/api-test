from flask import Blueprint, request, jsonify
from server.utils.csv_loader import load_csv
from server.services.search_service import search_in_dataframe

# Criar um Blueprint para a rota de busca
search_bp = Blueprint('search', __name__)

# Carregar o CSV uma vez ao iniciar o servidor
CSV_PATH = './preparationFiles/Relatorio_cadop.csv'
dataframe = load_csv(CSV_PATH)

@search_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({"error": "O parâmetro de busca 'q' é obrigatório."}), 400

    try:
        results = search_in_dataframe(dataframe, query)
        print(f"Resultados encontrados: {results}")  # Log para depuração
        return jsonify(results), 200
    except Exception as e:
        print(f"Erro: {e}")  # Log para depuração
        return jsonify({"error": str(e)}), 500