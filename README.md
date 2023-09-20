# Docker-And-Flask_JustForFun
This is a project that contains a simple python API and a SQL scripted database, all integrated into Docker containers

HTTP requests:
  /books
    - GET - request to get all books available

    CURL:
      curl http://localhost:your_choosen_web_port/books

  /books/id
    - GET - request to get a single book

    CURL:
      curl http://localhost:your_choosen_web_port/books/id

  /books/new
    - POST - request to post a new book and insert it into the database

    CURL:
      curl -X POST http://localhost:your_choosen_web_port/books/new -H "Content-Type:application/json"-d '{"author":"example", "id":1, "title":"example"}'

  /books/delete/id
    - DELETE - request to delete an available book

    CURL:
      curl -X DELETE http://localhost:your_choosen_web_port/books/delete/id -H "Content-Type:application/json"-d '{"author":"example", "id":1, "title":"example"}'

  /books/update/id
    - PUT - request to update an available book
    
    CURL:
      curl -X PUT http://localhost:your_choosen_web_port/books/update/id -H "Content-Type:application/json"-d '{"author":"example", "id":1, "title":"example"}'


