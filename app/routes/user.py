import json

from flask import request, Response

from app import app, database
from app.data import User
from app.encoder import EnhancedJSONEncoder


@app.route("/user/create", methods=['POST'])
def create_user():
    try:
        name = request.form['name']
        email = request.form['email']

        user = User(
            None,
            name,
            email
        )

        database.add_user(user)
        return Response(status=201)
    except:
        return Response(status=400)


@app.route("/user/<int:user_id>", methods=['PUT'])
def update_user(user_id):
    name = request.form['name']
    email = request.form['email']

    user = User(
        user_id,
        name,
        email
    )
    if database.update_user(user):
        return Response(status=200)

    return Response(status=404, response=json.dumps({'error': 'User not found'}), mimetype='application/json')


@app.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    try:
        user: User = database.get_user(user_id)
        return Response(status=200, response=json.dumps(user, cls=EnhancedJSONEncoder), mimetype='application/json')
    except FileNotFoundError:
        return Response(status=404, response=json.dumps({'error': 'User not found'}), mimetype='application/json')
