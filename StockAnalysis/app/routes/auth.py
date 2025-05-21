from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return jsonify({"message": "Login POST works"})
    else:
        return jsonify({"message": "Login GET works"})

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic here
        return jsonify({"message": "Register POST works"})
    else:
        return jsonify({"message": "Register GET works"})
