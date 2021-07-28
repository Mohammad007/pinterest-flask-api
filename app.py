# importing libraries
from flask import Flask, request, Response, jsonify
from py3pin.Pinterest import Pinterest

app = Flask(__name__)


@app.route('/')
def home():
   return "<center><h1>Welcome Pinterest API </h1></center>"

# Login function


@app.route('/login', methods=['POST'])

def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    username = data["username"]
    pinterest = Pinterest(email=email, password=password,
                          username=username, cred_root='cred_root')
    if email != '' and password != '' and username != '':
        pinterest.login()
        return jsonify({"message": "Thankyou for login", "status": 200})
    else:
        return jsonify({"message": "Please fill input", "status": 400})

if __name__ == '__main__':
   app.run(debug=True)
