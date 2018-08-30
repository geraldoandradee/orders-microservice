# Orders Microservice Documentation 

This project is a POC. Not production ready.


# Tests
    
To run the tests:
    
    $ pip install -r requirements/dev.txt
    $ flask run --host 0.0.0.0 --port 8888
    $ py.test -v

This project has only functional tests implemented.


# How to run

    $ cp .env.example .env
    $ docker-compose up --build
    
After you have to get token from /v1/auth

    $ curl -H "Content-Type: application/json" -X POST -d '{"username":"geraldo@geraldoandrade.com","password":"123456"}' http://localhost:5000/v1/auth
    $ {"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzU1MTQ5NjEsImlhdCI6MTUzNTUxNDY2MSwibmJmIjoxNTM1NTE0NjYxLCJpZGVudGl0eSI6ImdlcmFsZG9AZ2VyYWxkb2FuZHJhZGUuY29tIn0.F2bepYWo-kdoZRvIMuPoZLXAHRUuCCog_9d7NBq58ww"}

So you can get your generated access_token and use in your request:

    $ curl -XPOST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MzU1MTQ5NjEsImlhdCI6MTUzNTUxNDY2MSwibmJmIjoxNTM1NTE0NjYxLCJpZGVudGl0eSI6ImdlcmFsZG9AZ2VyYWxkb2FuZHJhZGUuY29tIn0.F2bepYWo-kdoZRvIMuPoZLXAHRUuCCog_9d7NBq58ww" \
    $ -d '{"id": 1333, "title": "Title here", "price": 1.22}' -H "Content-Type:application/json" http://localhost:5000/v1/orders