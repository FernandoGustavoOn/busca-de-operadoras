from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='../frontend/busca-operadoras/dist', static_url_path='')
CORS(app)  # Permite acesso do front-end

# Carregar o CSV (certifique-se de que o arquivo está na mesma pasta do app.py)
df = pd.read_csv("relatorio_cadop.csv", delimiter=";")
print(f"CSV carregado com {len(df)} registros")

@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    print("Rota /buscar acessada!")  # Log para verificar
    termo = request.args.get('termo', '').lower()
    
    # Filtrar por Razão Social ou Nome Fantasia
    resultados = df[df.apply(lambda x: termo in str(x['Razao_Social']).lower() or termo in str(x['Nome_Fantasia']).lower(), axis=1)]
    
    # Garantir que valores não válidos sejam substituídos
    resultados = resultados.fillna("Indisponível")  # Substituir NaN por "Indisponível"
    if resultados.empty:
        return jsonify({"mensagem": "Nenhum resultado encontrado para o termo pesquisado."})
    else:
        return jsonify(resultados.to_dict(orient="records"))

# Rota para servir o frontend
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Rota para servir arquivos estáticos
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
