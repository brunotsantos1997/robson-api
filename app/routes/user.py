import json

from flask import request, Response

from app import app, database
from app.data import User
from app.data.model import InvestmentClass
from app.encoder import EnhancedJSONEncoder
from app.xp_api import get_consolidated_investments, get_suitability_score


@app.route("/user/create", methods=['POST'])
def create_user():
    try:
        user_id = request.form['user_id']
        name = request.form['name']
        email = request.form['email']

        user = User(
            user_id,
            name,
            email
        )

        database.add_user(user)
        return Response(status=201)
    except:
        return Response(status=400)


@app.route("/user/<string:user_id>", methods=['PUT'])
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


@app.route("/user/<string:user_id>", methods=['GET'])
def get_user(user_id):
    try:
        user: User = database.get_user(user_id)
        return Response(status=200, response=json.dumps(user, cls=EnhancedJSONEncoder), mimetype='application/json')
    except FileNotFoundError:
        return Response(status=404, response=json.dumps({'error': 'User not found'}), mimetype='application/json')


@app.route('/user/<string:user_id>/allocation')
def get_allocation(user_id):
    investment = get_consolidated_investments(user_id)
    allocation = {
        'categories': {
            InvestmentClass.UNKNOWN.name: {'percentage': 0, 'amount': 0},
            InvestmentClass.VARIABLE_INCOME.name: {'percentage': 0, 'amount': 0},
            InvestmentClass.POST_FIXED.name: {'percentage': 0, 'amount': 0},
            InvestmentClass.MULTI_MARKET.name: {'percentage': 0, 'amount': 0},
            InvestmentClass.GLOBAL.name: {'percentage': 0, 'amount': 0},
            InvestmentClass.INFLATION.name: {'percentage': 0, 'amount': 0},
        },
        'total': 0.0
    }
    for i in investment:
        allocation['total'] += i.value
        allocation['categories'][i.classification.name]['amount'] += i.value

    for i in allocation['categories']:
        percentage = (allocation['categories'][i]['amount'] / allocation['total']) * 100
        allocation['categories'][i]['percentage'] = round(percentage, 2)

    return Response(status=200, response=json.dumps(lower_keys(allocation)), mimetype='application/json')


@app.route('/user/<string:user_id>/recommended_allocation')
def get_recommended_allocation(user_id):
    current_allocation = get_allocation(user_id).json
    suitability = get_suitability_score(user_id)
    if suitability > 25:
        recommended_allocation = {
            'categories': {
                InvestmentClass.UNKNOWN.name: {'amount': 0, 'percentage': 0},
                InvestmentClass.VARIABLE_INCOME.name: {'amount': 0, 'percentage': 40},
                InvestmentClass.POST_FIXED.name: {'amount': 0, 'percentage': 15},
                InvestmentClass.MULTI_MARKET.name: {'amount': 0, 'percentage': 10},
                InvestmentClass.GLOBAL.name: {'amount': 0, 'percentage': 20},
                InvestmentClass.INFLATION.name: {'amount': 0, 'percentage': 15},
            }
        }
    elif suitability > 5:
        recommended_allocation = {
            'categories': {
                InvestmentClass.UNKNOWN.name: {'amount': 0, 'percentage': 0},
                InvestmentClass.VARIABLE_INCOME.name: {'amount': 0, 'percentage': 20},
                InvestmentClass.POST_FIXED.name: {'amount': 0, 'percentage': 30},
                InvestmentClass.MULTI_MARKET.name: {'amount': 0, 'percentage': 20},
                InvestmentClass.GLOBAL.name: {'amount': 0, 'percentage': 10},
                InvestmentClass.INFLATION.name: {'amount': 0, 'percentage': 20},
            }
        }
    else:
        recommended_allocation = {
            'categories': {
                InvestmentClass.UNKNOWN.name: {'amount': 0, 'percentage': 0},
                InvestmentClass.VARIABLE_INCOME.name: {'amount': 0, 'percentage': 10},
                InvestmentClass.POST_FIXED.name: {'amount': 0, 'percentage': 50},
                InvestmentClass.MULTI_MARKET.name: {'amount': 0, 'percentage': 20},
                InvestmentClass.GLOBAL.name: {'amount': 0, 'percentage': 0},
                InvestmentClass.INFLATION.name: {'amount': 0, 'percentage': 20},
            }
        }

    recommended_allocation['total'] = current_allocation['total']
    for i in recommended_allocation['categories']:
        amount = recommended_allocation['total'] * (recommended_allocation['categories'][i]['percentage'] / 100)
        recommended_allocation['categories'][i]['amount'] = round(amount, 2)

    return Response(status=200, response=json.dumps(lower_keys(recommended_allocation)), mimetype='application/json')


def lower_keys(x):
    if isinstance(x, list):
        return [lower_keys(v) for v in x]
    elif isinstance(x, dict):
        return dict((k.lower(), lower_keys(v)) for k, v in x.items())
    else:
        return x
