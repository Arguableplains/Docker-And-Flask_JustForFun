from flask import Flask, jsonify, request
from databaseconnection import DBC

app = Flask(__name__)

#Utils

def json_formatter(response):

    list_json_done = []

    for line in response:
        
        json_done = {
        "id": line[0],
        "title": line[1],
        "author": line[2]
        }

        list_json_done.append(json_done)

    return list_json_done

@app.route('/books', methods=['GET'])
def get_books():

    with DBC() as db:
        answer = db.selecting_data()
        return jsonify(json_formatter(answer))

@app.route('/books/<int:id>', methods=['GET'])
def get_livros_id(id):

    with DBC() as db:
        answer = db.selecting_data_id(id)
        return jsonify(json_formatter(answer))

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):

    with DBC() as db:
        data_to_update = request.get_json()
        db.update_data(search=id, json_data=data_to_update)

    return get_books()

@app.route('/books/new', methods=['POST'])
def insert_new_book():

    with DBC() as db:
        db.inserting_data(request.get_json())

    return get_books()

@app.route('/books/<int:id>', methods=['DELETE'])
def excluir_livro(id):

    with DBC() as db:
        db.delete_data(id)

    return get_books()

app.run(port=5000, host='0.0.0.0', debug=True)