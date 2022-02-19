import json

import requests
from flask import Flask, request, Response
from database import DataBase
from model import Users
from model import Objective

app = Flask(__name__)

data_base = DataBase()
CNPJ_API = 'https://minhareceita.org/'
XP_TOKEN_API = 'https://openapi.xpi.com.br/oauth2/v1/access-token'


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


def get_investments():
    # TODO: "pra fazer"
    pass


@app.route("/user/create", methods=['POST'])
def create_user():
    try:
        user_id = int(request.form['user_id'])
        name = request.form['name']
        initial_date = request.form['initial_date']
        final_date = request.form['final_date']
        initial_investment = request.form['initial_investment']
        recurring_investment = request.form['recurring_investment']
        goal_value = request.form['goal_value']

        objective = Objective(None,
                              user_id,
                              name, initial_date,
                              final_date, initial_investment,
                              recurring_investment,
                              goal_value)

        data_base.add_objective(objective)
        return Response(status=201)
    except:
        return Response(status=400)


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

        objective = Objective(None,
                              user_id,
                              name, initial_date,
                              final_date, initial_investment,
                              recurring_investment,
                              goal_value)

        data_base.add_objective(objective)
        return Response(status=201)
    except:
        return Response(status=400)


def create_users():
    try:
        user_id = int(request.form['user_id'])
        name = request.form['name']
        email = request.form['email']

        objective = Objective(None,
                              user_id,
                              name,
                              email)

        data_base.add_objective(objective)
        return Response(status=201)
    except:
        return Response(status=400)


def get_xp_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Host': 'openapi.xpi.com.br',
    }
    data = {
        'client_id': '',
        'client_secret': '',
        'grant_type': 'client_credentials'
    }
    return requests.post(XP_TOKEN_API, headers=headers, data=data)


if __name__ == '__main__':
    app.run()
