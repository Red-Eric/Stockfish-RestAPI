from flask import Flask, jsonify, request
from engine_Stockfish import Engine
from flask_cors import CORS 


app = Flask(__name__)
CORS(app = app)

@app.route("/")
def welcome():
    return "Hello , this is a Simple Stockfish API"

@app.route("/best", methods = ["POST"])
def bestMove():
    data = request.get_json()
    print(data['fen'])
    stockfish = Engine()
    return jsonify(stockfish.get_Data(data['fen']))

if __name__ == "__main__":
    app.run()