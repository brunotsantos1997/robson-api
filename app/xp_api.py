import json
import statistics

import requests

from app.data.model import InvestmentClass, Investment
from .app import CLIENT_ID, CLIENT_SECRET, VERSION
from .constants import XP_TOKEN_API, XP_API_URL


def get_consolidated_investments(user_id):
    response = get_user_data(user_id)
    banks = response['banks']
    investments = []
    for bank in banks:
        for k, v in bank['investments'].items():
            for investment in v:
                investments.append(map_investment(investment, k))

    return investments


def get_suitability_score(user_id):
    user_data = get_user_data(user_id)
    suitabilities = []
    for bank in user_data['banks']:
        suitabilities.append(bank['suitability'])

    return statistics.median(suitabilities)


def map_investment(investment, investment_type):
    investment_class = InvestmentClass.UNKNOWN
    investment_dict = {
        'stocks': InvestmentClass.VARIABLE_INCOME,
        'cdb': InvestmentClass.POST_FIXED,
        'lci': InvestmentClass.POST_FIXED,
        'lca': InvestmentClass.POST_FIXED,
        'cri': InvestmentClass.INFLATION,
        'cra': InvestmentClass.INFLATION,
        'fii': InvestmentClass.VARIABLE_INCOME,
        'renda-variável': InvestmentClass.VARIABLE_INCOME,
        'multimercado': InvestmentClass.MULTI_MARKET,
        'renda-fixa': InvestmentClass.POST_FIXED,
        'privatePension': InvestmentClass.MULTI_MARKET,
    }

    if investment_type in investment_dict:
        investment_class = investment_dict[investment_type]
    elif investment_type == 'investmentFunds':
        investment_class = investment_dict[investment['type']]

    return Investment(
        identity=investment['identity'],
        bankId=investment['bankId'],
        description=investment.get('description', ''),
        type=investment.get('type', investment_type),
        classification=investment_class,
        value=investment['value'],
        dueDate=investment.get('dueDate', None),
        profitability=investment.get('profitability', None),
        risk=investment['risk'],
        acquisitionDate=investment['acquisitionDate'],
    )


def get_user_data(user_id):
    headers = {
        'Authorization': 'Bearer {}'.format(get_xp_token()),
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': f'Robson/{VERSION}',
    }
    response = requests.get(f'{XP_API_URL}/users/{user_id}', headers=headers)
    return response.json()


def get_xp_token():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Host': 'openapi.xpi.com.br',
        'User-Agent': f'Robson/{VERSION}',
    }
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response_content = json.loads(requests.post(XP_TOKEN_API, headers=headers, data=data).content)
    token = response_content['access_token']
    return token
