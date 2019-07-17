from flask import Blueprint, request, jsonify
from tasks import auth
from db import query
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['GET', 'POST'])
def auth_login():
    auth.add.delay(5, 10)
    if request.method == 'POST':
        return jsonify(dict(
            message='Auth Login POST Request'
        ))
    return jsonify(dict(
        message='Auth Login GET Request'
    ))
