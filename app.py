# importing libraries
from flask import Flask, request, Response, jsonify
from py3pin.Pinterest import Pinterest

app = Flask(__name__)


@app.route('/')
def home():
   return "<center><h1>Welcome Pinterest API </h1></center>"

# Login function
@app.route('/login', methods=['GET'])
def login():
    pinterest = Pinterest(email='bilalmalik1561@gmail.com',
                          password='bilal12345',
                          username='bilalmalik1561',
                          cred_root='cred_root')
    pinterest.login()
    return jsonify({"message": "Thankyou for login", "status": 200})
 

# Get border ID function
@app.route('/get_border_id', methods=['GET'])
def getBoardIds():
    pinterest = Pinterest(email='bilalmalik1561@gmail.com',
                          password='bilal12345',
                          username='bilalmalik1561',
                          cred_root='cred_root')
    username = "bilalmalik1561"

    if username != '':
            dictBoards = {}
            boards = pinterest.boards(username=username)
            for board in boards:
                dictBoards[board['name']] = board['id']
            return jsonify({"data": dictBoards, "status": 200})
    else:
        return jsonify({"message": "Please fill username", "status": 400})

if __name__ == '__main__':
   app.run(debug=True)
