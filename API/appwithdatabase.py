from flask import Flask, jsonify, request
from databaseconnection import DBC
import sys

sys.path.insert(0, "./../Database")


app = Flask(__name__)

#region Utils
"""
Here is where the responses from the database are formatted
And sended as http get requests, for now, shown on the terminal
or web navigator
"""

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

#endregion

#region Requests

#Return all the Books saved
@app.route('/books', methods=['GET'])
def get_books():

    with DBC() as db:
        answer = db.selecting_data()
        return jsonify(json_formatter(answer))

#Return a single book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_livros_id(id):

    with DBC() as db:
        answer = db.selecting_data_id(id)
        return jsonify(json_formatter(answer))
    
#Update a single book by the ID - needs the whole json with all informations
@app.route('/books/update/<int:id>', methods=['PUT'])
def update_book(id):

    with DBC() as db:
        data_to_update = request.get_json()
        db.update_data(search=id, json_data=data_to_update)

    return get_books()

#Add a single book to the database
@app.route('/books/new', methods=['POST'])
def insert_new_book():

    with DBC() as db:
        db.inserting_data(request.get_json())

    return get_books()

#Delete a single book by the ID
@app.route('/books/delete/<int:id>', methods=['DELETE'])
def excluir_livro(id):

    with DBC() as db:
        db.delete_data(id)

    return get_books()

#endregion

#Main Flask
app.run(port=5000, host='0.0.0.0', debug=True)

#port = web port which the api will listen to
#host = principal IP endress where the API will be hosted (localhost in this case)
#debug = this option enables the system responses from the API
#        to be seen on terminal