"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/log-in', methods=["POST"])
def check_user_identity():
    body = request.json
    email = body.get("email")
    password = body.get("password")
    if email is None:
        raise APIException("No email in body, 400")
    if password is None:
        raise APIException(400, "No password in body")
    user = User.query.filter_by(email=email).one_or_none()
    if user is None:
        raise APIException("No user in system, 404")
    if password != user.password:
        raise APIException(401, "Wrong password! STAY OUT")
    access_token = create_access_token(identity=user.id)
    return jsonify(
        access_token=access_token,
        user=user.serialize()
        ), 201

@api.route('/sign-up', methods=["POST"])
def user_sign_up():
    body = request.json
    email = body["email"]
    password = body["password"]
    
    if email is None:
        raise APIException("No email in body, 400")
    if password is None:
        raise APIException("No password in body, 400")
    user = User(email=email, password=password, is_active=True)
    

   
    db.session.add(user);
    db.session.commit();
    return jsonify(
        user.serialize()
    ), 201

    

@api.route("/transfers", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if user is None:
        raise APIException("No such user!, 404")
    return jsonify(logged_in_as=user.serialize()), 200