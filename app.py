# importing libraries
from flask import Flask, request, Response, jsonify
from py3pin.Pinterest import Pinterest

app = Flask(__name__)

# Login Pinterest
pinterest = Pinterest(email='bilalmalik1561@gmail.com',
                      password='bilal12345',
                      username='bilalmalik1561',
                      cred_root='cred_root')

username = "bilalmalik1561"


@app.route('/')
def home():
   return "<center><h1>Welcome Pinterest API </h1></center>"

# Login function
@app.route('/login', methods=['GET'])
def login():
    request_data = request.get_json()
    username = request_data['username']
    email = request_data['email']
    password = request_data['password']
    pinterest = Pinterest(email=email,
                          password=password,
                          username=username,
                          cred_root='cred_root')
    pinterest.login()
    return jsonify({"message": "Thankyou for login", "status": 200})


# Get border ID function
@app.route('/get_border_id', methods=['GET'])
def getBoardIds():
    request_data = request.get_json()
    username = request_data['username']
    dictBoards = {}
    boards = pinterest.boards(username=username)
    for board in boards:
        dictBoards[board['name']] = board['id']
    return jsonify({"data": dictBoards, "status": 200})

# get_user_profile function
@app.route('/get_user_profile', methods=['GET'])
def get_user_profile():
    request_data = request.get_json()
    username = request_data['username']
    return pinterest.get_user_overview(username=username)

# create_board function
@app.route('/create_board', methods=['GET'])
def create_board():
    request_data = request.get_json()
    name = request_data['name'],
    description = request_data['description']
    category = 'other',
    privacy = 'public',
    layout = 'default'
    if name != '' and description != '':
        pinterest.create_board(name=name, description=description, category=category,
                                  privacy=privacy, layout=layout)
        return jsonify({"message": "Board Create Successful", "status": 200})
    else:
        return jsonify({"message": "Please fill name and description", "status": 404})

# create_board_section function
@app.route('/create_board_section', methods=['GET'])
def create_board_section():
    request_data = request.get_json()
    board_id = request_data['board_id']
    section_name = request_data['section_name']

    if board_id != '' and section_name != '':
        pinterest.create_board_section(
            board_id=board_id, section_name=section_name)
        return jsonify({"message": "Board Section Create Successful", "status": 200})
    else:
        return jsonify({"message": "Please fill name and description", "status": 404})

# get_board_sections function
@app.route('/get_board_sections', methods=['GET'])
def get_board_sections():
    request_data = request.get_json()
    board_id = request_data['board_id']
    if board_id != '':
        data = pinterest.get_board_sections(board_id=board_id)
        return jsonify({"message": data, "status": 200})
    else:
        return jsonify({"message": "Please fill board_id", "status": 404})
    
# delete_board_section function
@app.route('/delete_board_section', methods=['GET'])
def delete_board_section():
    request_data = request.get_json()
    section_id = request_data['section_id']
    if section_id != '':
        pinterest.delete_board_section(section_id=section_id)
        return jsonify({"message": "Section Deleted!", "status": 200})
    else:
        return jsonify({"message": "Please fill section_id", "status": 404})


@app.route('/delete_board_section', methods=['POST'])
def pin():
    request_data = request.get_json()
    board_id = request_data['board_id']
    section_id = None
    image_url = request_data['image_url']
    description = request_data['description']
    title = request_data['title']
    link = request_data['link']
    if section_id != '':
        pinterest.pin(board_id=board_id, section_id=section_id, image_url=image_url, description=description,
                      title=title, link=link)
        return jsonify({"message": "Section Deleted!", "status": 200})
    else:
        return jsonify({"message": "Please fill all input", "status": 404})

if __name__ == '__main__':
   app.run(debug=True)
