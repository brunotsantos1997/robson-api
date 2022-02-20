import json

import requests
from flask import request, Response

from app import app, database, Objective
from app.constants import CNPJ_API
from app.xp_api import get_xp_token


@app.route("/objective/create", methods=['POST'])
def create_objective():
    try:
        user_id = int(request.form['user_id'])
        name = request.form['name']
        initial_date = request.form['initial_date']
        final_date = request.form['final_date']
        initial_investment = request.form['initial_investment']
        recurring_investment = request.form['recurring_investment']
        goal_value = request.form['goal_value']

        objective = Objective(
            None,
            user_id,
            name, initial_date,
            final_date, initial_investment,
            recurring_investment,
            goal_value
        )

        database.add_objective(objective)
        return Response(status=201)
    except:
        return Response(status=400)


@app.route("/objective/update", methods=['POST'])
def update_objective():
    try:
        user_id = int(request.form['user_id'])
        name = request.form['name']
        initial_date = request.form['initial_date']
        final_date = request.form['final_date']
        initial_investment = request.form['initial_investment']
        recurring_investment = request.form['recurring_investment']
        goal_value = request.form['goal_value']

        objective = Objective(
            None,
            user_id,
            name, initial_date,
            final_date, initial_investment,
            recurring_investment,
            goal_value
        )

        database.add_objective(objective)
        database.update_objective(objective)
        return Response(status=200)
    except:
        return Response(status=400)


@app.route("/objective/predict/<int:user_id>")
def objective_predict(user_id):
    cnpj_result = requests.get(CNPJ_API + '16501555000157')
    cnpj_info = json.loads(cnpj_result.content)
    get_xp_token()
    user_json = ""
    user_data = json.loads(user_json)

    banks = user_data['banks']
    pix_transactions = []
    for bank in banks:
        for pix in bank['pixHistory']:
            pix_transactions.append(pix)

    return cnpj_info['razao_social']
