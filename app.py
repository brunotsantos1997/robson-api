import json

import requests
from flask import Flask

app = Flask(__name__)

CNPJ_API = 'https://minhareceita.org/'
XP_TOKEN_API = 'https://openapi.xpi.com.br/oauth2/v1/access-token'


@app.route("/objective/predict/<int:user_id>")
def objective_predict(user_id):
    cnpj_result = requests.get(CNPJ_API + '16501555000157')
    cnpj_info = json.loads(cnpj_result.content)
    get_xp_token()
    user_json = """{
    "name": "JOAO",
    "cpf": "99999999991",
    "salary": 5087.48,
    "bornDate": "2001-04-14",
    "banks": [
        {
            "suitability": 78,
            "startDate": "2019-03-23",
            "institution": {
                "agency": "99999910",
                "number": "999999910",
                "bankId": "xp",
                "bankName": "xp"
            },
            "creditCard": {
                "limit": 17749.63,
                "transactions": [
                    {
                        "type": "refund",
                        "description": "",
                        "value": 18091.04,
                        "date": "2021-06-19"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 26607.46,
                        "date": "2021-12-30"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 12766.06,
                        "date": "2022-01-14"
                    }
                ],
                "revolvingCredit": 26794.44,
                "revolvingCreditTax": 0.05523097768473515,
                "installmentsUsage": false,
                "bills": []
            },
            "checking": {
                "balance": 207176.45,
                "limit": 123,
                "transactions": [
                    {
                        "type": "credit",
                        "description": "",
                        "value": 14528.68,
                        "date": "2021-07-15"
                    },
                    {
                        "type": "credit",
                        "description": "",
                        "value": 24158.32,
                        "date": "2021-08-19"
                    },
                    {
                        "type": "credit",
                        "description": "",
                        "value": 17284.32,
                        "date": "2021-04-22"
                    }
                ]
            },
            "saving": {
                "balance": 0
            },
            "pixHistory": [
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 85139.43,
                    "date": "2021-05-03"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 35496.15,
                    "date": "2021-05-09"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 80303.64,
                    "date": "2021-03-22"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 3096.03,
                    "date": "2021-09-13"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "description": "",
                    "value": 37722.54,
                    "date": "2021-07-20"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 49964.6,
                    "date": "2021-08-29"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 2205.77,
                    "date": "2021-02-25"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 45497.44,
                    "date": "2021-06-28"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 11543.32,
                    "date": "2021-03-02"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 49334,
                        "accountNumber": 368462,
                        "cpf": "99999999385"
                    },
                    "description": "",
                    "value": 13004.47,
                    "date": "2022-02-06"
                },
                {
                    "from": {
                        "bankName": "xp",
                        "agency": 99999910,
                        "accountNumber": 999999910,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "xp",
                        "agency": 99999903,
                        "accountNumber": 999999902,
                        "cpf": "002324545545"
                    },
                    "description": "",
                    "value": 0.001,
                    "date": "2022-02-18"
                }
            ],
            "consumedCreditLines": [
                {
                    "userId": "",
                    "bankId": "",
                    "type": "personal-loan",
                    "value": 13443.02,
                    "tax": 0.697096975211849,
                    "installments": 36,
                    "startDate": "2021-11-08",
                    "endDate": "2022-03-01"
                }
            ],
            "investments": {
                "stocks": [
                    {
                        "identity": "xp-stocks-0-99999999991",
                        "bankId": "xp",
                        "ticker": "DAA49",
                        "volumn": 961,
                        "value": 95,
                        "acquisitionDate": "2020-07-08",
                        "risk": 51
                    },
                    {
                        "identity": "xp-stocks-1-99999999991",
                        "bankId": "xp",
                        "ticker": "FAB31",
                        "volumn": 4381,
                        "value": 81,
                        "acquisitionDate": "2020-12-19",
                        "risk": 63
                    },
                    {
                        "identity": "xp-stocks-2-99999999991",
                        "bankId": "xp",
                        "ticker": "AAC33",
                        "volumn": 1094,
                        "value": 17,
                        "acquisitionDate": "2019-12-18",
                        "risk": 27
                    },
                    {
                        "identity": "xp-stocks-3-99999999991",
                        "bankId": "xp",
                        "ticker": "PAD91",
                        "volumn": 3645,
                        "value": 105,
                        "acquisitionDate": "2021-03-22",
                        "risk": 72
                    }
                ],
                "cdb": [
                    {
                        "identity": "xp-Cdb-0-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 166,
                        "dueDate": "2023-05-18",
                        "profitability": 0,
                        "risk": 52,
                        "acquisitionDate": "2020-06-28",
                        "volumn": 7023
                    },
                    {
                        "identity": "xp-Cdb-1-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 250,
                        "dueDate": "2023-10-18",
                        "profitability": 0,
                        "risk": 20,
                        "acquisitionDate": "2021-08-11",
                        "volumn": 8329
                    },
                    {
                        "identity": "xp-Cdb-2-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 257,
                        "dueDate": "2023-05-13",
                        "profitability": 0,
                        "risk": 77,
                        "acquisitionDate": "2019-11-30",
                        "volumn": 129
                    },
                    {
                        "identity": "xp-Cdb-3-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 144,
                        "dueDate": "2023-07-24",
                        "profitability": 0,
                        "risk": 30,
                        "acquisitionDate": "2020-05-09",
                        "volumn": 5433
                    },
                    {
                        "identity": "xp-Cdb-4-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 119,
                        "dueDate": "2024-08-05",
                        "profitability": 0,
                        "risk": 47,
                        "acquisitionDate": "2020-07-22",
                        "volumn": 5041
                    },
                    {
                        "identity": "xp-Cdb-5-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 181,
                        "dueDate": "2023-10-16",
                        "profitability": 0,
                        "risk": 66,
                        "acquisitionDate": "2021-03-08",
                        "volumn": 5635
                    },
                    {
                        "identity": "xp-Cdb-6-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 86,
                        "dueDate": "2023-11-14",
                        "profitability": 0,
                        "risk": 62,
                        "acquisitionDate": "2019-10-16",
                        "volumn": 7681
                    },
                    {
                        "identity": "xp-Cdb-7-99999999991",
                        "bankId": "xp",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 98,
                        "dueDate": "2022-09-19",
                        "profitability": 0,
                        "risk": 37,
                        "acquisitionDate": "2019-12-19",
                        "volumn": 924
                    }
                ],
                "investmentFunds": [
                    {
                        "identity": "xp-investfund-0-99999999991",
                        "bankId": "xp",
                        "name": "fii 0",
                        "type": "fii",
                        "value": 107,
                        "acquisitionDate": "2020-02-20",
                        "risk": 27,
                        "volumn": 961
                    },
                    {
                        "identity": "xp-investfund-1-99999999991",
                        "bankId": "xp",
                        "name": "renda-fixa 1",
                        "type": "renda-fixa",
                        "value": 45,
                        "acquisitionDate": "2021-06-21",
                        "risk": 21,
                        "volumn": 7788
                    },
                    {
                        "identity": "xp-investfund-2-99999999991",
                        "bankId": "xp",
                        "name": "renda-variável 2",
                        "type": "renda-variável",
                        "value": 93,
                        "acquisitionDate": "2020-03-20",
                        "risk": 36,
                        "volumn": 4075
                    },
                    {
                        "identity": "xp-investfund-3-99999999991",
                        "bankId": "xp",
                        "name": "multimercado 3",
                        "type": "multimercado",
                        "value": 66,
                        "acquisitionDate": "2020-10-12",
                        "risk": 10,
                        "volumn": 1357
                    }
                ],
                "savingsAccount": [],
                "privatePension": [],
                "lci": [
                    {
                        "identity": "xp-Lci-0-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 71,
                        "dueDate": "2023-08-24",
                        "profitability": 0,
                        "risk": 10,
                        "acquisitionDate": "2021-04-16",
                        "volumn": 365
                    },
                    {
                        "identity": "xp-Lci-1-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 241,
                        "dueDate": "2024-02-24",
                        "profitability": 0,
                        "risk": 96,
                        "acquisitionDate": "2020-08-26",
                        "volumn": 8909
                    },
                    {
                        "identity": "xp-Lci-2-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 207,
                        "dueDate": "2024-02-21",
                        "profitability": 0,
                        "risk": 38,
                        "acquisitionDate": "2020-08-05",
                        "volumn": 9189
                    },
                    {
                        "identity": "xp-Lci-3-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 91,
                        "dueDate": "2023-06-21",
                        "profitability": 0,
                        "risk": 70,
                        "acquisitionDate": "2020-07-16",
                        "volumn": 612
                    },
                    {
                        "identity": "xp-Lci-4-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 133,
                        "dueDate": "2023-07-09",
                        "profitability": 0,
                        "risk": 21,
                        "acquisitionDate": "2020-12-29",
                        "volumn": 2053
                    },
                    {
                        "identity": "xp-Lci-5-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 88,
                        "dueDate": "2024-07-30",
                        "profitability": 0,
                        "risk": 39,
                        "acquisitionDate": "2019-09-09",
                        "volumn": 9409
                    },
                    {
                        "identity": "xp-Lci-6-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 160,
                        "dueDate": "2024-05-16",
                        "profitability": 0,
                        "risk": 92,
                        "acquisitionDate": "2020-08-15",
                        "volumn": 5307
                    },
                    {
                        "identity": "xp-Lci-7-99999999991",
                        "bankId": "xp",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 68,
                        "dueDate": "2023-11-24",
                        "profitability": 0,
                        "risk": 16,
                        "acquisitionDate": "2021-07-09",
                        "volumn": 4731
                    }
                ],
                "lca": [
                    {
                        "identity": "xp-Lca-0-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 139,
                        "dueDate": "2024-04-30",
                        "profitability": 0,
                        "risk": 34,
                        "acquisitionDate": "2020-06-21",
                        "volumn": 6015
                    },
                    {
                        "identity": "xp-Lca-1-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 186,
                        "dueDate": "2024-02-01",
                        "profitability": 0,
                        "risk": 56,
                        "acquisitionDate": "2020-04-18",
                        "volumn": 6642
                    },
                    {
                        "identity": "xp-Lca-2-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 104,
                        "dueDate": "2024-05-09",
                        "profitability": 0,
                        "risk": 38,
                        "acquisitionDate": "2020-05-30",
                        "volumn": 301
                    },
                    {
                        "identity": "xp-Lca-3-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 254,
                        "dueDate": "2024-03-02",
                        "profitability": 0,
                        "risk": 32,
                        "acquisitionDate": "2020-07-25",
                        "volumn": 1799
                    },
                    {
                        "identity": "xp-Lca-4-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 201,
                        "dueDate": "2023-12-08",
                        "profitability": 0,
                        "risk": 28,
                        "acquisitionDate": "2020-07-19",
                        "volumn": 6610
                    },
                    {
                        "identity": "xp-Lca-5-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 143,
                        "dueDate": "2023-05-11",
                        "profitability": 0,
                        "risk": 41,
                        "acquisitionDate": "2021-07-15",
                        "volumn": 3058
                    },
                    {
                        "identity": "xp-Lca-6-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 247,
                        "dueDate": "2023-02-09",
                        "profitability": 0,
                        "risk": 29,
                        "acquisitionDate": "2020-12-28",
                        "volumn": 7736
                    },
                    {
                        "identity": "xp-Lca-7-99999999991",
                        "bankId": "xp",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 107,
                        "dueDate": "2022-08-21",
                        "profitability": 0,
                        "risk": 78,
                        "acquisitionDate": "2019-09-10",
                        "volumn": 6101
                    }
                ],
                "cri": [
                    {
                        "identity": "xp-Cri-0-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 249,
                        "dueDate": "2023-10-10",
                        "profitability": 0,
                        "risk": 40,
                        "acquisitionDate": "2021-08-16",
                        "volumn": 1026
                    },
                    {
                        "identity": "xp-Cri-1-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 218,
                        "dueDate": "2023-01-01",
                        "profitability": 0,
                        "risk": 57,
                        "acquisitionDate": "2020-10-14",
                        "volumn": 4708
                    },
                    {
                        "identity": "xp-Cri-2-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 156,
                        "dueDate": "2023-09-22",
                        "profitability": 0,
                        "risk": 20,
                        "acquisitionDate": "2020-04-30",
                        "volumn": 4397
                    },
                    {
                        "identity": "xp-Cri-3-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 65,
                        "dueDate": "2024-06-06",
                        "profitability": 0,
                        "risk": 0,
                        "acquisitionDate": "2020-05-27",
                        "volumn": 9900
                    },
                    {
                        "identity": "xp-Cri-4-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 71,
                        "dueDate": "2023-12-24",
                        "profitability": 0,
                        "risk": 25,
                        "acquisitionDate": "2020-12-17",
                        "volumn": 9576
                    },
                    {
                        "identity": "xp-Cri-5-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 194,
                        "dueDate": "2024-06-15",
                        "profitability": 0,
                        "risk": 15,
                        "acquisitionDate": "2020-09-18",
                        "volumn": 3580
                    },
                    {
                        "identity": "xp-Cri-6-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 90,
                        "dueDate": "2023-10-10",
                        "profitability": 0,
                        "risk": 49,
                        "acquisitionDate": "2020-12-01",
                        "volumn": 4950
                    },
                    {
                        "identity": "xp-Cri-7-99999999991",
                        "bankId": "xp",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 169,
                        "dueDate": "2023-04-14",
                        "profitability": 0,
                        "risk": 27,
                        "acquisitionDate": "2020-09-30",
                        "volumn": 8052
                    }
                ],
                "cra": [
                    {
                        "identity": "xp-Cra-0-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 139,
                        "dueDate": "2023-02-17",
                        "profitability": 0,
                        "risk": 75,
                        "acquisitionDate": "2020-06-12",
                        "volumn": 1164
                    },
                    {
                        "identity": "xp-Cra-1-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 174,
                        "dueDate": "2024-06-08",
                        "profitability": 0,
                        "risk": 14,
                        "acquisitionDate": "2020-07-01",
                        "volumn": 6027
                    },
                    {
                        "identity": "xp-Cra-2-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 184,
                        "dueDate": "2023-06-08",
                        "profitability": 0,
                        "risk": 43,
                        "acquisitionDate": "2020-07-22",
                        "volumn": 9036
                    },
                    {
                        "identity": "xp-Cra-3-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 155,
                        "dueDate": "2023-03-21",
                        "profitability": 0,
                        "risk": 48,
                        "acquisitionDate": "2019-12-28",
                        "volumn": 7902
                    },
                    {
                        "identity": "xp-Cra-4-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 167,
                        "dueDate": "2024-02-19",
                        "profitability": 0,
                        "risk": 33,
                        "acquisitionDate": "2021-05-28",
                        "volumn": 1577
                    },
                    {
                        "identity": "xp-Cra-5-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 107,
                        "dueDate": "2023-05-03",
                        "profitability": 0,
                        "risk": 57,
                        "acquisitionDate": "2021-08-04",
                        "volumn": 2964
                    },
                    {
                        "identity": "xp-Cra-6-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 209,
                        "dueDate": "2023-03-08",
                        "profitability": 0,
                        "risk": 72,
                        "acquisitionDate": "2020-05-15",
                        "volumn": 268
                    },
                    {
                        "identity": "xp-Cra-7-99999999991",
                        "bankId": "xp",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 233,
                        "dueDate": "2024-07-01",
                        "profitability": 0,
                        "risk": 81,
                        "acquisitionDate": "2021-08-11",
                        "volumn": 2650
                    }
                ]
            },
            "bills": [
                {
                    "identity": "99999999991-0",
                    "value": 22542.47,
                    "startDate": "2020-04-05",
                    "paidDate": "2021-10-13"
                },
                {
                    "identity": "99999999991-1",
                    "value": 82219.55,
                    "startDate": "2020-09-30",
                    "paidDate": "2022-01-17"
                },
                {
                    "identity": "99999999991-2",
                    "value": 4003.13,
                    "startDate": "2020-07-14",
                    "paidDate": "2021-05-06"
                },
                {
                    "identity": "99999999991-3",
                    "value": 92281.76,
                    "startDate": "2020-08-07",
                    "paidDate": "2022-02-07"
                },
                {
                    "identity": "99999999991-4",
                    "value": 71985.39,
                    "startDate": "2020-11-09",
                    "paidDate": "2021-05-19"
                },
                {
                    "identity": "99999999991-5",
                    "value": 73788.44,
                    "startDate": "2021-02-14",
                    "paidDate": "2021-12-26"
                },
                {
                    "identity": "99999999991-6",
                    "value": 95373.96,
                    "startDate": "2020-09-27",
                    "paidDate": "2022-01-08"
                },
                {
                    "identity": "99999999991-7",
                    "value": 23804.13,
                    "startDate": "2020-06-18",
                    "paidDate": "2021-09-03"
                },
                {
                    "identity": "99999999991-8",
                    "value": 93757.63,
                    "startDate": "2020-12-16",
                    "paidDate": "2021-03-09"
                },
                {
                    "identity": "99999999991-9",
                    "value": 39262.39,
                    "startDate": "2020-11-11",
                    "paidDate": "2022-01-18"
                }
            ]
        },
        {
            "suitability": 46,
            "startDate": "2019-09-26",
            "institution": {
                "agency": "99999911",
                "number": "999999911",
                "bankId": "bank-a",
                "bankName": "bank-a"
            },
            "creditCard": {
                "limit": 9238.97,
                "transactions": [
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 6156.25,
                        "date": "2021-10-06"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 27621.56,
                        "date": "2022-02-10"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 16719.5,
                        "date": "2021-04-01"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 3027.1,
                        "date": "2021-11-13"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 27898.25,
                        "date": "2021-10-21"
                    }
                ],
                "revolvingCredit": 27216.01,
                "revolvingCreditTax": 0.03235352985367828,
                "installmentsUsage": false,
                "bills": []
            },
            "checking": {
                "balance": 346398.2,
                "limit": 21866.54,
                "transactions": [
                    {
                        "type": "debit",
                        "description": "",
                        "value": 1384.9,
                        "date": "2021-07-17"
                    },
                    {
                        "type": "credit",
                        "description": "",
                        "value": 26962.87,
                        "date": "2021-04-29"
                    },
                    {
                        "type": "credit",
                        "description": "",
                        "value": 19529.97,
                        "date": "2021-02-26"
                    },
                    {
                        "type": "credit",
                        "description": "",
                        "value": 594.28,
                        "date": "2021-10-26"
                    },
                    {
                        "type": "credit",
                        "description": "",
                        "value": 15791.67,
                        "date": "2021-05-04"
                    }
                ]
            },
            "saving": {
                "balance": 0
            },
            "pixHistory": [
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "description": "",
                    "value": 6411.29,
                    "date": "2022-01-28"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "description": "",
                    "value": 50741.07,
                    "date": "2021-10-21"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "description": "",
                    "value": 81033.79,
                    "date": "2021-10-01"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 4149.01,
                    "date": "2021-08-23"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "description": "",
                    "value": 58852.29,
                    "date": "2021-03-24"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "description": "",
                    "value": 74652.95,
                    "date": "2021-05-14"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "description": "",
                    "value": 84143.39,
                    "date": "2021-06-09"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 82242.02,
                    "date": "2022-01-04"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 92778.15,
                    "date": "2021-10-19"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 76842,
                        "accountNumber": 235118,
                        "cpf": "99999999658"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 99999911,
                        "accountNumber": 999999911,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 12947.83,
                    "date": "2021-05-30"
                }
            ],
            "consumedCreditLines": [
                {
                    "userId": "",
                    "bankId": "",
                    "type": "personal-loan",
                    "value": 22930.37,
                    "tax": 0.239326279014508,
                    "installments": 6,
                    "startDate": "2021-11-14",
                    "endDate": "2022-03-16"
                }
            ],
            "investments": {
                "stocks": [
                    {
                        "identity": "bank-a-stocks-0-99999999991",
                        "bankId": "bank-a",
                        "ticker": "DAA37",
                        "volumn": 4384,
                        "value": 81,
                        "acquisitionDate": "2021-04-02",
                        "risk": 50
                    },
                    {
                        "identity": "bank-a-stocks-1-99999999991",
                        "bankId": "bank-a",
                        "ticker": "NAB82",
                        "volumn": 3052,
                        "value": 71,
                        "acquisitionDate": "2021-06-01",
                        "risk": 88
                    },
                    {
                        "identity": "bank-a-stocks-2-99999999991",
                        "bankId": "bank-a",
                        "ticker": "TAC52",
                        "volumn": 6868,
                        "value": 38,
                        "acquisitionDate": "2019-12-19",
                        "risk": 64
                    },
                    {
                        "identity": "bank-a-stocks-3-99999999991",
                        "bankId": "bank-a",
                        "ticker": "LAD37",
                        "volumn": 7581,
                        "value": 46,
                        "acquisitionDate": "2021-04-19",
                        "risk": 75
                    }
                ],
                "cdb": [
                    {
                        "identity": "bank-a-Cdb-0-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 174,
                        "dueDate": "2022-12-19",
                        "profitability": 0,
                        "risk": 69,
                        "acquisitionDate": "2020-04-22",
                        "volumn": 7684
                    },
                    {
                        "identity": "bank-a-Cdb-1-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 186,
                        "dueDate": "2023-11-02",
                        "profitability": 0,
                        "risk": 55,
                        "acquisitionDate": "2020-05-22",
                        "volumn": 5639
                    },
                    {
                        "identity": "bank-a-Cdb-2-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 223,
                        "dueDate": "2022-12-11",
                        "profitability": 0,
                        "risk": 22,
                        "acquisitionDate": "2020-12-26",
                        "volumn": 5522
                    },
                    {
                        "identity": "bank-a-Cdb-3-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 168,
                        "dueDate": "2022-10-30",
                        "profitability": 0,
                        "risk": 23,
                        "acquisitionDate": "2020-05-09",
                        "volumn": 7818
                    },
                    {
                        "identity": "bank-a-Cdb-4-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 157,
                        "dueDate": "2024-01-29",
                        "profitability": 0,
                        "risk": 88,
                        "acquisitionDate": "2021-08-05",
                        "volumn": 5946
                    },
                    {
                        "identity": "bank-a-Cdb-5-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 110,
                        "dueDate": "2023-01-16",
                        "profitability": 0,
                        "risk": 0,
                        "acquisitionDate": "2020-02-21",
                        "volumn": 9584
                    },
                    {
                        "identity": "bank-a-Cdb-6-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 78,
                        "dueDate": "2023-10-21",
                        "profitability": 0,
                        "risk": 31,
                        "acquisitionDate": "2020-10-26",
                        "volumn": 8986
                    },
                    {
                        "identity": "bank-a-Cdb-7-99999999991",
                        "bankId": "bank-a",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 177,
                        "dueDate": "2024-01-27",
                        "profitability": 0,
                        "risk": 42,
                        "acquisitionDate": "2019-12-03",
                        "volumn": 9212
                    }
                ],
                "investmentFunds": [
                    {
                        "identity": "bank-a-investfund-0-99999999991",
                        "bankId": "bank-a",
                        "name": "fii 0",
                        "type": "fii",
                        "value": 96,
                        "acquisitionDate": "2020-06-04",
                        "risk": 28,
                        "volumn": 7723
                    },
                    {
                        "identity": "bank-a-investfund-1-99999999991",
                        "bankId": "bank-a",
                        "name": "renda-fixa 1",
                        "type": "renda-fixa",
                        "value": 48,
                        "acquisitionDate": "2019-09-22",
                        "risk": 60,
                        "volumn": 7571
                    },
                    {
                        "identity": "bank-a-investfund-2-99999999991",
                        "bankId": "bank-a",
                        "name": "renda-variável 2",
                        "type": "renda-variável",
                        "value": 59,
                        "acquisitionDate": "2020-06-06",
                        "risk": 86,
                        "volumn": 5026
                    },
                    {
                        "identity": "bank-a-investfund-3-99999999991",
                        "bankId": "bank-a",
                        "name": "multimercado 3",
                        "type": "multimercado",
                        "value": 123,
                        "acquisitionDate": "2020-11-27",
                        "risk": 97,
                        "volumn": 3766
                    }
                ],
                "savingsAccount": [],
                "privatePension": [],
                "lci": [
                    {
                        "identity": "bank-a-Lci-0-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 213,
                        "dueDate": "2024-02-04",
                        "profitability": 0,
                        "risk": 19,
                        "acquisitionDate": "2020-09-28",
                        "volumn": 8514
                    },
                    {
                        "identity": "bank-a-Lci-1-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 250,
                        "dueDate": "2023-03-19",
                        "profitability": 0,
                        "risk": 33,
                        "acquisitionDate": "2021-05-10",
                        "volumn": 1334
                    },
                    {
                        "identity": "bank-a-Lci-2-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 172,
                        "dueDate": "2022-11-29",
                        "profitability": 0,
                        "risk": 67,
                        "acquisitionDate": "2020-10-26",
                        "volumn": 1720
                    },
                    {
                        "identity": "bank-a-Lci-3-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 95,
                        "dueDate": "2024-02-21",
                        "profitability": 0,
                        "risk": 20,
                        "acquisitionDate": "2020-06-19",
                        "volumn": 6221
                    },
                    {
                        "identity": "bank-a-Lci-4-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 94,
                        "dueDate": "2024-04-24",
                        "profitability": 0,
                        "risk": 98,
                        "acquisitionDate": "2020-12-09",
                        "volumn": 7119
                    },
                    {
                        "identity": "bank-a-Lci-5-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 175,
                        "dueDate": "2023-07-11",
                        "profitability": 0,
                        "risk": 58,
                        "acquisitionDate": "2020-03-13",
                        "volumn": 2722
                    },
                    {
                        "identity": "bank-a-Lci-6-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 236,
                        "dueDate": "2022-10-15",
                        "profitability": 0,
                        "risk": 87,
                        "acquisitionDate": "2021-05-25",
                        "volumn": 8545
                    },
                    {
                        "identity": "bank-a-Lci-7-99999999991",
                        "bankId": "bank-a",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 222,
                        "dueDate": "2024-01-11",
                        "profitability": 0,
                        "risk": 41,
                        "acquisitionDate": "2020-11-03",
                        "volumn": 1637
                    }
                ],
                "lca": [
                    {
                        "identity": "bank-a-Lca-0-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 259,
                        "dueDate": "2023-04-10",
                        "profitability": 0,
                        "risk": 50,
                        "acquisitionDate": "2021-03-18",
                        "volumn": 2347
                    },
                    {
                        "identity": "bank-a-Lca-1-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 149,
                        "dueDate": "2024-07-17",
                        "profitability": 0,
                        "risk": 80,
                        "acquisitionDate": "2021-01-16",
                        "volumn": 3121
                    },
                    {
                        "identity": "bank-a-Lca-2-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 248,
                        "dueDate": "2024-03-04",
                        "profitability": 0,
                        "risk": 23,
                        "acquisitionDate": "2021-05-09",
                        "volumn": 8883
                    },
                    {
                        "identity": "bank-a-Lca-3-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 134,
                        "dueDate": "2023-01-01",
                        "profitability": 0,
                        "risk": 15,
                        "acquisitionDate": "2021-05-03",
                        "volumn": 4752
                    },
                    {
                        "identity": "bank-a-Lca-4-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 189,
                        "dueDate": "2022-12-05",
                        "profitability": 0,
                        "risk": 69,
                        "acquisitionDate": "2020-09-16",
                        "volumn": 8285
                    },
                    {
                        "identity": "bank-a-Lca-5-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 205,
                        "dueDate": "2023-09-05",
                        "profitability": 0,
                        "risk": 87,
                        "acquisitionDate": "2019-10-01",
                        "volumn": 2877
                    },
                    {
                        "identity": "bank-a-Lca-6-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 107,
                        "dueDate": "2023-07-03",
                        "profitability": 0,
                        "risk": 91,
                        "acquisitionDate": "2021-03-12",
                        "volumn": 9700
                    },
                    {
                        "identity": "bank-a-Lca-7-99999999991",
                        "bankId": "bank-a",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 112,
                        "dueDate": "2022-11-18",
                        "profitability": 0,
                        "risk": 27,
                        "acquisitionDate": "2019-12-31",
                        "volumn": 3567
                    }
                ],
                "cri": [
                    {
                        "identity": "bank-a-Cri-0-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 259,
                        "dueDate": "2022-11-28",
                        "profitability": 0,
                        "risk": 75,
                        "acquisitionDate": "2020-11-01",
                        "volumn": 5877
                    },
                    {
                        "identity": "bank-a-Cri-1-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 199,
                        "dueDate": "2023-12-04",
                        "profitability": 0,
                        "risk": 92,
                        "acquisitionDate": "2020-10-11",
                        "volumn": 4092
                    },
                    {
                        "identity": "bank-a-Cri-2-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 230,
                        "dueDate": "2024-05-18",
                        "profitability": 0,
                        "risk": 58,
                        "acquisitionDate": "2021-08-11",
                        "volumn": 1383
                    },
                    {
                        "identity": "bank-a-Cri-3-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 154,
                        "dueDate": "2024-01-03",
                        "profitability": 0,
                        "risk": 81,
                        "acquisitionDate": "2019-11-21",
                        "volumn": 4426
                    },
                    {
                        "identity": "bank-a-Cri-4-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 251,
                        "dueDate": "2024-02-23",
                        "profitability": 0,
                        "risk": 66,
                        "acquisitionDate": "2020-11-24",
                        "volumn": 9690
                    },
                    {
                        "identity": "bank-a-Cri-5-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 103,
                        "dueDate": "2024-06-14",
                        "profitability": 0,
                        "risk": 46,
                        "acquisitionDate": "2020-07-22",
                        "volumn": 3433
                    },
                    {
                        "identity": "bank-a-Cri-6-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 163,
                        "dueDate": "2024-02-10",
                        "profitability": 0,
                        "risk": 20,
                        "acquisitionDate": "2020-09-30",
                        "volumn": 3968
                    },
                    {
                        "identity": "bank-a-Cri-7-99999999991",
                        "bankId": "bank-a",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 163,
                        "dueDate": "2022-09-27",
                        "profitability": 0,
                        "risk": 71,
                        "acquisitionDate": "2020-06-08",
                        "volumn": 1877
                    }
                ],
                "cra": [
                    {
                        "identity": "bank-a-Cra-0-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 89,
                        "dueDate": "2024-05-21",
                        "profitability": 0,
                        "risk": 11,
                        "acquisitionDate": "2021-07-05",
                        "volumn": 4601
                    },
                    {
                        "identity": "bank-a-Cra-1-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 199,
                        "dueDate": "2023-11-30",
                        "profitability": 0,
                        "risk": 20,
                        "acquisitionDate": "2020-03-09",
                        "volumn": 9473
                    },
                    {
                        "identity": "bank-a-Cra-2-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 123,
                        "dueDate": "2024-01-20",
                        "profitability": 0,
                        "risk": 87,
                        "acquisitionDate": "2020-07-26",
                        "volumn": 1081
                    },
                    {
                        "identity": "bank-a-Cra-3-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 194,
                        "dueDate": "2024-02-03",
                        "profitability": 0,
                        "risk": 78,
                        "acquisitionDate": "2020-06-20",
                        "volumn": 9868
                    },
                    {
                        "identity": "bank-a-Cra-4-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 167,
                        "dueDate": "2022-10-26",
                        "profitability": 0,
                        "risk": 76,
                        "acquisitionDate": "2020-01-23",
                        "volumn": 3673
                    },
                    {
                        "identity": "bank-a-Cra-5-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 89,
                        "dueDate": "2022-10-17",
                        "profitability": 0,
                        "risk": 19,
                        "acquisitionDate": "2020-12-27",
                        "volumn": 4924
                    },
                    {
                        "identity": "bank-a-Cra-6-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 61,
                        "dueDate": "2024-07-08",
                        "profitability": 0,
                        "risk": 20,
                        "acquisitionDate": "2021-05-01",
                        "volumn": 5755
                    },
                    {
                        "identity": "bank-a-Cra-7-99999999991",
                        "bankId": "bank-a",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 166,
                        "dueDate": "2024-02-18",
                        "profitability": 0,
                        "risk": 37,
                        "acquisitionDate": "2020-03-11",
                        "volumn": 7841
                    }
                ]
            },
            "bills": [
                {
                    "identity": "99999999991-0",
                    "value": 44085.28,
                    "startDate": "2020-06-04",
                    "paidDate": "2021-07-19"
                },
                {
                    "identity": "99999999991-1",
                    "value": 54073.46,
                    "startDate": "2021-02-02",
                    "paidDate": "2021-08-31"
                },
                {
                    "identity": "99999999991-2",
                    "value": 41673.46,
                    "startDate": "2020-10-04",
                    "paidDate": "2021-10-02"
                },
                {
                    "identity": "99999999991-3",
                    "value": 59650.58,
                    "startDate": "2020-09-01",
                    "paidDate": "2021-05-20"
                },
                {
                    "identity": "99999999991-4",
                    "value": 50434.67,
                    "startDate": "2021-01-20",
                    "paidDate": "2022-01-21"
                },
                {
                    "identity": "99999999991-5",
                    "value": 33847.97,
                    "startDate": "2020-12-01",
                    "paidDate": "2021-05-04"
                },
                {
                    "identity": "99999999991-6",
                    "value": 6192.51,
                    "startDate": "2020-11-23",
                    "paidDate": "2022-02-05"
                },
                {
                    "identity": "99999999991-7",
                    "value": 94156.75,
                    "startDate": "2020-03-24",
                    "paidDate": "2021-07-03"
                },
                {
                    "identity": "99999999991-8",
                    "value": 21561.52,
                    "startDate": "2020-10-24",
                    "paidDate": "2021-11-20"
                },
                {
                    "identity": "99999999991-9",
                    "value": 62834.25,
                    "startDate": "2020-10-07",
                    "paidDate": "2021-08-12"
                }
            ]
        },
        {
            "suitability": 21,
            "startDate": "2019-05-07",
            "institution": {
                "agency": "99999912",
                "number": "999999912",
                "bankId": "bank-b",
                "bankName": "bank-b"
            },
            "creditCard": {
                "limit": 3252.09,
                "transactions": [
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 24043.37,
                        "date": "2021-08-22"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 23724.02,
                        "date": "2021-09-17"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 23696.15,
                        "date": "2022-01-10"
                    }
                ],
                "revolvingCredit": 17101.14,
                "revolvingCreditTax": 0.013387354840137533,
                "installmentsUsage": true,
                "bills": []
            },
            "checking": {
                "balance": 0,
                "limit": 0,
                "transactions": []
            },
            "saving": {
                "balance": 775788
            },
            "pixHistory": [
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 64613.05,
                    "date": "2021-04-03"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 81467.78,
                    "date": "2021-11-16"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 15261.63,
                    "date": "2021-10-06"
                },
                {
                    "from": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "description": "",
                    "value": 92674.99,
                    "date": "2021-05-12"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 65349.18,
                    "date": "2021-05-29"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 39755.14,
                    "date": "2021-12-07"
                },
                {
                    "from": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "description": "",
                    "value": 90434.42,
                    "date": "2021-10-10"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 43871.96,
                    "date": "2021-09-06"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 20365.99,
                    "date": "2021-08-04"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 36294,
                        "accountNumber": 264942,
                        "cpf": "99999999927"
                    },
                    "to": {
                        "bankName": "bank-b",
                        "agency": 99999912,
                        "accountNumber": 999999912,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 45057.63,
                    "date": "2021-08-12"
                }
            ],
            "consumedCreditLines": [
                {
                    "userId": "",
                    "bankId": "",
                    "type": "personal-loan",
                    "value": 22951.01,
                    "tax": 0.318732240636379,
                    "installments": 23,
                    "startDate": "2021-08-27",
                    "endDate": "2022-04-05"
                }
            ],
            "investments": {
                "stocks": [
                    {
                        "identity": "bank-b-stocks-0-99999999991",
                        "bankId": "bank-b",
                        "ticker": "YAA20",
                        "volumn": 5415,
                        "value": 74,
                        "acquisitionDate": "2021-02-01",
                        "risk": 29
                    },
                    {
                        "identity": "bank-b-stocks-1-99999999991",
                        "bankId": "bank-b",
                        "ticker": "KAB96",
                        "volumn": 5968,
                        "value": 25,
                        "acquisitionDate": "2021-05-02",
                        "risk": 36
                    },
                    {
                        "identity": "bank-b-stocks-2-99999999991",
                        "bankId": "bank-b",
                        "ticker": "NAC66",
                        "volumn": 993,
                        "value": 75,
                        "acquisitionDate": "2021-04-20",
                        "risk": 38
                    },
                    {
                        "identity": "bank-b-stocks-3-99999999991",
                        "bankId": "bank-b",
                        "ticker": "UAD81",
                        "volumn": 439,
                        "value": 84,
                        "acquisitionDate": "2019-10-04",
                        "risk": 65
                    }
                ],
                "cdb": [
                    {
                        "identity": "bank-b-Cdb-0-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 142,
                        "dueDate": "2023-03-07",
                        "profitability": 0,
                        "risk": 80,
                        "acquisitionDate": "2020-06-28",
                        "volumn": 3110
                    },
                    {
                        "identity": "bank-b-Cdb-1-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 116,
                        "dueDate": "2023-09-28",
                        "profitability": 0,
                        "risk": 88,
                        "acquisitionDate": "2021-02-24",
                        "volumn": 2469
                    },
                    {
                        "identity": "bank-b-Cdb-2-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 149,
                        "dueDate": "2023-09-27",
                        "profitability": 0,
                        "risk": 24,
                        "acquisitionDate": "2021-02-21",
                        "volumn": 9885
                    },
                    {
                        "identity": "bank-b-Cdb-3-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 141,
                        "dueDate": "2023-12-28",
                        "profitability": 0,
                        "risk": 28,
                        "acquisitionDate": "2020-08-17",
                        "volumn": 7561
                    },
                    {
                        "identity": "bank-b-Cdb-4-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 79,
                        "dueDate": "2022-11-12",
                        "profitability": 0,
                        "risk": 31,
                        "acquisitionDate": "2021-06-23",
                        "volumn": 4631
                    },
                    {
                        "identity": "bank-b-Cdb-5-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 128,
                        "dueDate": "2022-09-08",
                        "profitability": 0,
                        "risk": 92,
                        "acquisitionDate": "2020-06-11",
                        "volumn": 588
                    },
                    {
                        "identity": "bank-b-Cdb-6-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 200,
                        "dueDate": "2023-02-23",
                        "profitability": 0,
                        "risk": 96,
                        "acquisitionDate": "2020-03-05",
                        "volumn": 2186
                    },
                    {
                        "identity": "bank-b-Cdb-7-99999999991",
                        "bankId": "bank-b",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 253,
                        "dueDate": "2023-12-26",
                        "profitability": 0,
                        "risk": 36,
                        "acquisitionDate": "2021-02-21",
                        "volumn": 6450
                    }
                ],
                "investmentFunds": [
                    {
                        "identity": "bank-b-investfund-0-99999999991",
                        "bankId": "bank-b",
                        "name": "fii 0",
                        "type": "fii",
                        "value": 106,
                        "acquisitionDate": "2020-09-29",
                        "risk": 78,
                        "volumn": 2752
                    },
                    {
                        "identity": "bank-b-investfund-1-99999999991",
                        "bankId": "bank-b",
                        "name": "renda-fixa 1",
                        "type": "renda-fixa",
                        "value": 152,
                        "acquisitionDate": "2020-07-07",
                        "risk": 22,
                        "volumn": 1276
                    },
                    {
                        "identity": "bank-b-investfund-2-99999999991",
                        "bankId": "bank-b",
                        "name": "renda-variável 2",
                        "type": "renda-variável",
                        "value": 88,
                        "acquisitionDate": "2021-05-24",
                        "risk": 46,
                        "volumn": 5217
                    },
                    {
                        "identity": "bank-b-investfund-3-99999999991",
                        "bankId": "bank-b",
                        "name": "multimercado 3",
                        "type": "multimercado",
                        "value": 79,
                        "acquisitionDate": "2020-03-05",
                        "risk": 36,
                        "volumn": 9794
                    }
                ],
                "savingsAccount": [],
                "privatePension": [],
                "lci": [
                    {
                        "identity": "bank-b-Lci-0-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 243,
                        "dueDate": "2024-06-24",
                        "profitability": 0,
                        "risk": 58,
                        "acquisitionDate": "2020-02-17",
                        "volumn": 124
                    },
                    {
                        "identity": "bank-b-Lci-1-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 197,
                        "dueDate": "2023-07-09",
                        "profitability": 0,
                        "risk": 11,
                        "acquisitionDate": "2020-07-23",
                        "volumn": 1770
                    },
                    {
                        "identity": "bank-b-Lci-2-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 122,
                        "dueDate": "2023-03-19",
                        "profitability": 0,
                        "risk": 57,
                        "acquisitionDate": "2019-10-09",
                        "volumn": 58
                    },
                    {
                        "identity": "bank-b-Lci-3-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 126,
                        "dueDate": "2024-03-21",
                        "profitability": 0,
                        "risk": 27,
                        "acquisitionDate": "2020-05-25",
                        "volumn": 9480
                    },
                    {
                        "identity": "bank-b-Lci-4-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 88,
                        "dueDate": "2023-01-08",
                        "profitability": 0,
                        "risk": 31,
                        "acquisitionDate": "2019-11-29",
                        "volumn": 5092
                    },
                    {
                        "identity": "bank-b-Lci-5-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 107,
                        "dueDate": "2024-06-21",
                        "profitability": 0,
                        "risk": 81,
                        "acquisitionDate": "2020-10-11",
                        "volumn": 2801
                    },
                    {
                        "identity": "bank-b-Lci-6-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 175,
                        "dueDate": "2023-07-30",
                        "profitability": 0,
                        "risk": 38,
                        "acquisitionDate": "2021-01-02",
                        "volumn": 5935
                    },
                    {
                        "identity": "bank-b-Lci-7-99999999991",
                        "bankId": "bank-b",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 215,
                        "dueDate": "2022-10-20",
                        "profitability": 0,
                        "risk": 34,
                        "acquisitionDate": "2020-12-24",
                        "volumn": 902
                    }
                ],
                "lca": [
                    {
                        "identity": "bank-b-Lca-0-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 241,
                        "dueDate": "2023-08-17",
                        "profitability": 0,
                        "risk": 26,
                        "acquisitionDate": "2021-08-03",
                        "volumn": 6101
                    },
                    {
                        "identity": "bank-b-Lca-1-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 167,
                        "dueDate": "2023-12-20",
                        "profitability": 0,
                        "risk": 26,
                        "acquisitionDate": "2020-09-15",
                        "volumn": 5317
                    },
                    {
                        "identity": "bank-b-Lca-2-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 151,
                        "dueDate": "2023-01-28",
                        "profitability": 0,
                        "risk": 69,
                        "acquisitionDate": "2021-01-16",
                        "volumn": 9418
                    },
                    {
                        "identity": "bank-b-Lca-3-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 150,
                        "dueDate": "2022-09-27",
                        "profitability": 0,
                        "risk": 24,
                        "acquisitionDate": "2019-11-09",
                        "volumn": 1764
                    },
                    {
                        "identity": "bank-b-Lca-4-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 77,
                        "dueDate": "2023-10-07",
                        "profitability": 0,
                        "risk": 92,
                        "acquisitionDate": "2020-08-09",
                        "volumn": 9482
                    },
                    {
                        "identity": "bank-b-Lca-5-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 221,
                        "dueDate": "2023-02-23",
                        "profitability": 0,
                        "risk": 58,
                        "acquisitionDate": "2020-12-18",
                        "volumn": 5196
                    },
                    {
                        "identity": "bank-b-Lca-6-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 89,
                        "dueDate": "2024-06-30",
                        "profitability": 0,
                        "risk": 71,
                        "acquisitionDate": "2020-10-10",
                        "volumn": 111
                    },
                    {
                        "identity": "bank-b-Lca-7-99999999991",
                        "bankId": "bank-b",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 128,
                        "dueDate": "2023-12-22",
                        "profitability": 0,
                        "risk": 67,
                        "acquisitionDate": "2020-08-14",
                        "volumn": 5220
                    }
                ],
                "cri": [
                    {
                        "identity": "bank-b-Cri-0-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 206,
                        "dueDate": "2022-10-30",
                        "profitability": 0,
                        "risk": 60,
                        "acquisitionDate": "2019-12-28",
                        "volumn": 6826
                    },
                    {
                        "identity": "bank-b-Cri-1-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 78,
                        "dueDate": "2023-07-07",
                        "profitability": 0,
                        "risk": 0,
                        "acquisitionDate": "2020-06-20",
                        "volumn": 1994
                    },
                    {
                        "identity": "bank-b-Cri-2-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 230,
                        "dueDate": "2023-01-13",
                        "profitability": 0,
                        "risk": 67,
                        "acquisitionDate": "2021-01-02",
                        "volumn": 8351
                    },
                    {
                        "identity": "bank-b-Cri-3-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 118,
                        "dueDate": "2023-04-04",
                        "profitability": 0,
                        "risk": 2,
                        "acquisitionDate": "2019-11-21",
                        "volumn": 1212
                    },
                    {
                        "identity": "bank-b-Cri-4-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 141,
                        "dueDate": "2024-07-12",
                        "profitability": 0,
                        "risk": 83,
                        "acquisitionDate": "2020-02-07",
                        "volumn": 988
                    },
                    {
                        "identity": "bank-b-Cri-5-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 172,
                        "dueDate": "2022-10-29",
                        "profitability": 0,
                        "risk": 4,
                        "acquisitionDate": "2021-01-22",
                        "volumn": 4100
                    },
                    {
                        "identity": "bank-b-Cri-6-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 134,
                        "dueDate": "2023-10-28",
                        "profitability": 0,
                        "risk": 99,
                        "acquisitionDate": "2021-06-09",
                        "volumn": 5270
                    },
                    {
                        "identity": "bank-b-Cri-7-99999999991",
                        "bankId": "bank-b",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 112,
                        "dueDate": "2023-04-03",
                        "profitability": 0,
                        "risk": 46,
                        "acquisitionDate": "2021-04-01",
                        "volumn": 2990
                    }
                ],
                "cra": [
                    {
                        "identity": "bank-b-Cra-0-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 157,
                        "dueDate": "2024-02-10",
                        "profitability": 0,
                        "risk": 42,
                        "acquisitionDate": "2020-12-27",
                        "volumn": 4540
                    },
                    {
                        "identity": "bank-b-Cra-1-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 200,
                        "dueDate": "2024-03-23",
                        "profitability": 0,
                        "risk": 50,
                        "acquisitionDate": "2020-06-16",
                        "volumn": 9259
                    },
                    {
                        "identity": "bank-b-Cra-2-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 185,
                        "dueDate": "2023-06-12",
                        "profitability": 0,
                        "risk": 94,
                        "acquisitionDate": "2020-03-02",
                        "volumn": 3691
                    },
                    {
                        "identity": "bank-b-Cra-3-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 209,
                        "dueDate": "2023-02-24",
                        "profitability": 0,
                        "risk": 83,
                        "acquisitionDate": "2020-06-30",
                        "volumn": 8833
                    },
                    {
                        "identity": "bank-b-Cra-4-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 70,
                        "dueDate": "2024-03-25",
                        "profitability": 0,
                        "risk": 74,
                        "acquisitionDate": "2020-02-17",
                        "volumn": 3670
                    },
                    {
                        "identity": "bank-b-Cra-5-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 207,
                        "dueDate": "2024-05-28",
                        "profitability": 0,
                        "risk": 93,
                        "acquisitionDate": "2020-11-02",
                        "volumn": 9639
                    },
                    {
                        "identity": "bank-b-Cra-6-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 110,
                        "dueDate": "2023-12-11",
                        "profitability": 0,
                        "risk": 30,
                        "acquisitionDate": "2019-09-17",
                        "volumn": 318
                    },
                    {
                        "identity": "bank-b-Cra-7-99999999991",
                        "bankId": "bank-b",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 205,
                        "dueDate": "2023-05-15",
                        "profitability": 0,
                        "risk": 75,
                        "acquisitionDate": "2020-03-27",
                        "volumn": 9473
                    }
                ]
            },
            "bills": [
                {
                    "identity": "99999999991-0",
                    "value": 2283.23,
                    "startDate": "2020-12-19",
                    "paidDate": "2021-06-28"
                },
                {
                    "identity": "99999999991-1",
                    "value": 19766.91,
                    "startDate": "2020-12-21",
                    "paidDate": "2021-08-20"
                },
                {
                    "identity": "99999999991-2",
                    "value": 99728.18,
                    "startDate": "2020-10-28",
                    "paidDate": "2021-08-09"
                },
                {
                    "identity": "99999999991-3",
                    "value": 55187.06,
                    "startDate": "2020-12-23",
                    "paidDate": "2021-05-03"
                },
                {
                    "identity": "99999999991-4",
                    "value": 35332.02,
                    "startDate": "2020-10-07",
                    "paidDate": "2021-09-19"
                },
                {
                    "identity": "99999999991-5",
                    "value": 12329.28,
                    "startDate": "2020-11-21",
                    "paidDate": "2021-07-30"
                },
                {
                    "identity": "99999999991-6",
                    "value": 97474.87,
                    "startDate": "2020-11-21",
                    "paidDate": "2021-12-12"
                },
                {
                    "identity": "99999999991-7",
                    "value": 71913.16,
                    "startDate": "2020-04-01",
                    "paidDate": "2021-09-18"
                },
                {
                    "identity": "99999999991-8",
                    "value": 69708.8,
                    "startDate": "2020-04-20",
                    "paidDate": "2021-06-27"
                },
                {
                    "identity": "99999999991-9",
                    "value": 18425.39,
                    "startDate": "2021-01-26",
                    "paidDate": "2022-01-08"
                }
            ]
        },
        {
            "suitability": 74,
            "startDate": "2017-12-02",
            "institution": {
                "agency": "99999913",
                "number": "999999913",
                "bankId": "bank-c",
                "bankName": "bank-c"
            },
            "creditCard": {
                "limit": 30256.33,
                "transactions": [
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 18120.06,
                        "date": "2021-11-11"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 27968.77,
                        "date": "2022-01-27"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 15874.85,
                        "date": "2021-07-18"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 5162.95,
                        "date": "2021-06-02"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 26693.39,
                        "date": "2021-02-23"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 1427.84,
                        "date": "2021-06-18"
                    },
                    {
                        "type": "purchase",
                        "description": "",
                        "value": 18140.04,
                        "date": "2021-12-25"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 8347.2,
                        "date": "2021-12-02"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 8919.17,
                        "date": "2021-05-12"
                    },
                    {
                        "type": "refund",
                        "description": "",
                        "value": 29392.09,
                        "date": "2021-08-09"
                    }
                ],
                "revolvingCredit": 29600.47,
                "revolvingCreditTax": 0.06205138654626932,
                "installmentsUsage": true,
                "bills": []
            },
            "checking": {
                "balance": 0,
                "limit": 0,
                "transactions": []
            },
            "saving": {
                "balance": 1018272
            },
            "pixHistory": [
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 73158.85,
                    "date": "2021-10-23"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 18585.62,
                    "date": "2021-08-23"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 41983.75,
                    "date": "2021-04-24"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 84520.89,
                    "date": "2021-11-29"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 21109.13,
                    "date": "2022-01-06"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 89482.15,
                    "date": "2021-10-16"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 55513.87,
                    "date": "2021-09-06"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 92143.78,
                    "date": "2021-05-07"
                },
                {
                    "from": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "to": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "description": "",
                    "value": 17067.18,
                    "date": "2022-01-13"
                },
                {
                    "from": {
                        "bankName": "bank-c",
                        "agency": 99999913,
                        "accountNumber": 999999913,
                        "cpf": "99999999991"
                    },
                    "to": {
                        "bankName": "bank-a",
                        "agency": 70777,
                        "accountNumber": 524164,
                        "cpf": "99999999988"
                    },
                    "description": "",
                    "value": 38232.66,
                    "date": "2022-02-04"
                }
            ],
            "consumedCreditLines": [
                {
                    "userId": "",
                    "bankId": "",
                    "type": "leasing",
                    "value": 25886.51,
                    "tax": 0.115876515314453,
                    "installments": 5,
                    "startDate": "2021-04-29",
                    "endDate": "2022-09-05"
                }
            ],
            "investments": {
                "stocks": [
                    {
                        "identity": "bank-c-stocks-0-99999999991",
                        "bankId": "bank-c",
                        "ticker": "WAA38",
                        "volumn": 4581,
                        "value": 32,
                        "acquisitionDate": "2021-07-28",
                        "risk": 33
                    },
                    {
                        "identity": "bank-c-stocks-1-99999999991",
                        "bankId": "bank-c",
                        "ticker": "KAB55",
                        "volumn": 6659,
                        "value": 32,
                        "acquisitionDate": "2020-02-14",
                        "risk": 79
                    },
                    {
                        "identity": "bank-c-stocks-2-99999999991",
                        "bankId": "bank-c",
                        "ticker": "HAC51",
                        "volumn": 9299,
                        "value": 75,
                        "acquisitionDate": "2021-05-26",
                        "risk": 27
                    },
                    {
                        "identity": "bank-c-stocks-3-99999999991",
                        "bankId": "bank-c",
                        "ticker": "JAD60",
                        "volumn": 7872,
                        "value": 89,
                        "acquisitionDate": "2021-03-25",
                        "risk": 49
                    }
                ],
                "cdb": [
                    {
                        "identity": "bank-c-Cdb-0-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 197,
                        "dueDate": "2022-11-26",
                        "profitability": 0,
                        "risk": 69,
                        "acquisitionDate": "2020-09-18",
                        "volumn": 9179
                    },
                    {
                        "identity": "bank-c-Cdb-1-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 122,
                        "dueDate": "2023-06-22",
                        "profitability": 0,
                        "risk": 95,
                        "acquisitionDate": "2021-03-01",
                        "volumn": 9492
                    },
                    {
                        "identity": "bank-c-Cdb-2-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 164,
                        "dueDate": "2023-12-06",
                        "profitability": 0,
                        "risk": 90,
                        "acquisitionDate": "2020-12-08",
                        "volumn": 8821
                    },
                    {
                        "identity": "bank-c-Cdb-3-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 177,
                        "dueDate": "2022-10-16",
                        "profitability": 0,
                        "risk": 83,
                        "acquisitionDate": "2021-07-13",
                        "volumn": 4572
                    },
                    {
                        "identity": "bank-c-Cdb-4-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 100,
                        "dueDate": "2023-07-12",
                        "profitability": 0,
                        "risk": 16,
                        "acquisitionDate": "2021-06-12",
                        "volumn": 9904
                    },
                    {
                        "identity": "bank-c-Cdb-5-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 213,
                        "dueDate": "2024-01-19",
                        "profitability": 0,
                        "risk": 65,
                        "acquisitionDate": "2020-07-23",
                        "volumn": 5251
                    },
                    {
                        "identity": "bank-c-Cdb-6-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 133,
                        "dueDate": "2022-11-01",
                        "profitability": 0,
                        "risk": 1,
                        "acquisitionDate": "2021-07-03",
                        "volumn": 7448
                    },
                    {
                        "identity": "bank-c-Cdb-7-99999999991",
                        "bankId": "bank-c",
                        "description": "Cdb",
                        "type": "Cdb",
                        "value": 142,
                        "dueDate": "2023-01-07",
                        "profitability": 0,
                        "risk": 45,
                        "acquisitionDate": "2020-01-25",
                        "volumn": 8379
                    }
                ],
                "investmentFunds": [
                    {
                        "identity": "bank-c-investfund-0-99999999991",
                        "bankId": "bank-c",
                        "name": "fii 0",
                        "type": "fii",
                        "value": 23,
                        "acquisitionDate": "2020-03-03",
                        "risk": 45,
                        "volumn": 536
                    },
                    {
                        "identity": "bank-c-investfund-1-99999999991",
                        "bankId": "bank-c",
                        "name": "renda-fixa 1",
                        "type": "renda-fixa",
                        "value": 105,
                        "acquisitionDate": "2019-12-05",
                        "risk": 70,
                        "volumn": 2727
                    },
                    {
                        "identity": "bank-c-investfund-2-99999999991",
                        "bankId": "bank-c",
                        "name": "renda-variável 2",
                        "type": "renda-variável",
                        "value": 59,
                        "acquisitionDate": "2020-09-29",
                        "risk": 49,
                        "volumn": 5060
                    },
                    {
                        "identity": "bank-c-investfund-3-99999999991",
                        "bankId": "bank-c",
                        "name": "multimercado 3",
                        "type": "multimercado",
                        "value": 63,
                        "acquisitionDate": "2020-08-12",
                        "risk": 67,
                        "volumn": 3855
                    }
                ],
                "savingsAccount": [],
                "privatePension": [],
                "lci": [
                    {
                        "identity": "bank-c-Lci-0-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 63,
                        "dueDate": "2023-06-17",
                        "profitability": 0,
                        "risk": 86,
                        "acquisitionDate": "2021-08-10",
                        "volumn": 2342
                    },
                    {
                        "identity": "bank-c-Lci-1-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 75,
                        "dueDate": "2023-05-16",
                        "profitability": 0,
                        "risk": 1,
                        "acquisitionDate": "2021-02-21",
                        "volumn": 3568
                    },
                    {
                        "identity": "bank-c-Lci-2-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 239,
                        "dueDate": "2023-09-18",
                        "profitability": 0,
                        "risk": 58,
                        "acquisitionDate": "2021-04-29",
                        "volumn": 9790
                    },
                    {
                        "identity": "bank-c-Lci-3-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 127,
                        "dueDate": "2023-10-20",
                        "profitability": 0,
                        "risk": 36,
                        "acquisitionDate": "2021-07-15",
                        "volumn": 2379
                    },
                    {
                        "identity": "bank-c-Lci-4-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 93,
                        "dueDate": "2023-03-25",
                        "profitability": 0,
                        "risk": 71,
                        "acquisitionDate": "2021-08-17",
                        "volumn": 6993
                    },
                    {
                        "identity": "bank-c-Lci-5-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 124,
                        "dueDate": "2024-06-26",
                        "profitability": 0,
                        "risk": 77,
                        "acquisitionDate": "2021-01-20",
                        "volumn": 9897
                    },
                    {
                        "identity": "bank-c-Lci-6-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 202,
                        "dueDate": "2023-02-20",
                        "profitability": 0,
                        "risk": 39,
                        "acquisitionDate": "2020-12-27",
                        "volumn": 4941
                    },
                    {
                        "identity": "bank-c-Lci-7-99999999991",
                        "bankId": "bank-c",
                        "description": "Lci",
                        "type": "Lci",
                        "value": 190,
                        "dueDate": "2024-03-03",
                        "profitability": 0,
                        "risk": 99,
                        "acquisitionDate": "2021-06-20",
                        "volumn": 1148
                    }
                ],
                "lca": [
                    {
                        "identity": "bank-c-Lca-0-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 158,
                        "dueDate": "2023-06-07",
                        "profitability": 0,
                        "risk": 10,
                        "acquisitionDate": "2019-12-01",
                        "volumn": 5295
                    },
                    {
                        "identity": "bank-c-Lca-1-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 242,
                        "dueDate": "2023-04-06",
                        "profitability": 0,
                        "risk": 46,
                        "acquisitionDate": "2019-12-15",
                        "volumn": 8682
                    },
                    {
                        "identity": "bank-c-Lca-2-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 254,
                        "dueDate": "2023-01-25",
                        "profitability": 0,
                        "risk": 73,
                        "acquisitionDate": "2021-02-17",
                        "volumn": 5042
                    },
                    {
                        "identity": "bank-c-Lca-3-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 191,
                        "dueDate": "2023-06-22",
                        "profitability": 0,
                        "risk": 31,
                        "acquisitionDate": "2021-03-25",
                        "volumn": 1050
                    },
                    {
                        "identity": "bank-c-Lca-4-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 222,
                        "dueDate": "2024-03-27",
                        "profitability": 0,
                        "risk": 42,
                        "acquisitionDate": "2020-10-02",
                        "volumn": 1167
                    },
                    {
                        "identity": "bank-c-Lca-5-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 234,
                        "dueDate": "2024-04-14",
                        "profitability": 0,
                        "risk": 81,
                        "acquisitionDate": "2020-08-05",
                        "volumn": 9185
                    },
                    {
                        "identity": "bank-c-Lca-6-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 190,
                        "dueDate": "2022-09-07",
                        "profitability": 0,
                        "risk": 72,
                        "acquisitionDate": "2020-03-12",
                        "volumn": 1394
                    },
                    {
                        "identity": "bank-c-Lca-7-99999999991",
                        "bankId": "bank-c",
                        "description": "Lca",
                        "type": "Lca",
                        "value": 133,
                        "dueDate": "2023-04-15",
                        "profitability": 0,
                        "risk": 49,
                        "acquisitionDate": "2021-08-07",
                        "volumn": 7501
                    }
                ],
                "cri": [
                    {
                        "identity": "bank-c-Cri-0-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 200,
                        "dueDate": "2023-10-18",
                        "profitability": 0,
                        "risk": 100,
                        "acquisitionDate": "2021-08-12",
                        "volumn": 9911
                    },
                    {
                        "identity": "bank-c-Cri-1-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 84,
                        "dueDate": "2023-09-09",
                        "profitability": 0,
                        "risk": 17,
                        "acquisitionDate": "2020-03-07",
                        "volumn": 4114
                    },
                    {
                        "identity": "bank-c-Cri-2-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 181,
                        "dueDate": "2023-07-16",
                        "profitability": 0,
                        "risk": 57,
                        "acquisitionDate": "2020-11-15",
                        "volumn": 376
                    },
                    {
                        "identity": "bank-c-Cri-3-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 223,
                        "dueDate": "2023-03-22",
                        "profitability": 0,
                        "risk": 61,
                        "acquisitionDate": "2020-04-29",
                        "volumn": 9081
                    },
                    {
                        "identity": "bank-c-Cri-4-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 80,
                        "dueDate": "2024-07-07",
                        "profitability": 0,
                        "risk": 66,
                        "acquisitionDate": "2019-09-07",
                        "volumn": 8608
                    },
                    {
                        "identity": "bank-c-Cri-5-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 195,
                        "dueDate": "2023-12-24",
                        "profitability": 0,
                        "risk": 47,
                        "acquisitionDate": "2021-04-07",
                        "volumn": 4562
                    },
                    {
                        "identity": "bank-c-Cri-6-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 176,
                        "dueDate": "2024-05-11",
                        "profitability": 0,
                        "risk": 55,
                        "acquisitionDate": "2020-06-03",
                        "volumn": 6629
                    },
                    {
                        "identity": "bank-c-Cri-7-99999999991",
                        "bankId": "bank-c",
                        "description": "Cri",
                        "type": "Cri",
                        "value": 218,
                        "dueDate": "2024-06-26",
                        "profitability": 0,
                        "risk": 95,
                        "acquisitionDate": "2020-12-28",
                        "volumn": 9195
                    }
                ],
                "cra": [
                    {
                        "identity": "bank-c-Cra-0-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 116,
                        "dueDate": "2024-01-20",
                        "profitability": 0,
                        "risk": 1,
                        "acquisitionDate": "2019-10-14",
                        "volumn": 5659
                    },
                    {
                        "identity": "bank-c-Cra-1-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 115,
                        "dueDate": "2022-11-15",
                        "profitability": 0,
                        "risk": 91,
                        "acquisitionDate": "2020-05-23",
                        "volumn": 11
                    },
                    {
                        "identity": "bank-c-Cra-2-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 259,
                        "dueDate": "2022-11-06",
                        "profitability": 0,
                        "risk": 44,
                        "acquisitionDate": "2020-10-10",
                        "volumn": 6635
                    },
                    {
                        "identity": "bank-c-Cra-3-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 76,
                        "dueDate": "2023-02-18",
                        "profitability": 0,
                        "risk": 95,
                        "acquisitionDate": "2020-03-09",
                        "volumn": 3811
                    },
                    {
                        "identity": "bank-c-Cra-4-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 71,
                        "dueDate": "2023-05-31",
                        "profitability": 0,
                        "risk": 89,
                        "acquisitionDate": "2021-03-23",
                        "volumn": 4348
                    },
                    {
                        "identity": "bank-c-Cra-5-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 220,
                        "dueDate": "2023-12-05",
                        "profitability": 0,
                        "risk": 93,
                        "acquisitionDate": "2020-01-24",
                        "volumn": 5529
                    },
                    {
                        "identity": "bank-c-Cra-6-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 151,
                        "dueDate": "2023-02-05",
                        "profitability": 0,
                        "risk": 55,
                        "acquisitionDate": "2021-03-13",
                        "volumn": 4148
                    },
                    {
                        "identity": "bank-c-Cra-7-99999999991",
                        "bankId": "bank-c",
                        "description": "Cra",
                        "type": "Cra",
                        "value": 193,
                        "dueDate": "2023-01-12",
                        "profitability": 0,
                        "risk": 40,
                        "acquisitionDate": "2020-04-06",
                        "volumn": 1233
                    }
                ]
            },
            "bills": [
                {
                    "identity": "99999999991-0",
                    "value": 81946.13,
                    "startDate": "2020-09-23",
                    "paidDate": "2021-12-01"
                },
                {
                    "identity": "99999999991-1",
                    "value": 31367.42,
                    "startDate": "2020-11-14",
                    "paidDate": "2021-05-01"
                },
                {
                    "identity": "99999999991-2",
                    "value": 61697.15,
                    "startDate": "2020-12-07",
                    "paidDate": "2021-11-28"
                },
                {
                    "identity": "99999999991-3",
                    "value": 57076.9,
                    "startDate": "2020-04-12",
                    "paidDate": "2021-08-28"
                },
                {
                    "identity": "99999999991-4",
                    "value": 3595.78,
                    "startDate": "2020-04-22",
                    "paidDate": "2022-02-02"
                },
                {
                    "identity": "99999999991-5",
                    "value": 85234.12,
                    "startDate": "2020-08-29",
                    "paidDate": "2021-05-21"
                },
                {
                    "identity": "99999999991-6",
                    "value": 68991.89,
                    "startDate": "2020-04-12",
                    "paidDate": "2021-07-10"
                },
                {
                    "identity": "99999999991-7",
                    "value": 54367,
                    "startDate": "2020-12-11",
                    "paidDate": "2021-08-02"
                },
                {
                    "identity": "99999999991-8",
                    "value": 67382.92,
                    "startDate": "2020-04-26",
                    "paidDate": "2021-12-22"
                },
                {
                    "identity": "99999999991-9",
                    "value": 54135.7,
                    "startDate": "2020-02-28",
                    "paidDate": "2021-10-31"
                }
            ]
        }
    ]
}"""
    user_data = json.loads(user_json)

    banks = user_data['banks']
    pix_transactions = []
    for bank in banks:
        for pix in bank['pixHistory']:
            pix_transactions.append(pix)

    return cnpj_info['razao_social']


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
