from app.app import app
from app.ai.transactions import generate_clusters
from app.cnpj_api import get_cnpj_cnaes_description
from app.data import database
from app.data.model import Transaction, UserTransactions
from app.xp_api import get_user_pix_transactions


@app.route("/ai/cluster/")
def clusterize_users():
    # user_transactions_list = get_all_user_transactions()
    # using mock data because cnpj is not available in XP's openbanking api, but it could be used to get cnpj's cnaes
    user_transactions_list = mock_user_transactions_list()

    return f'{generate_clusters(user_transactions_list, 2)}'


def get_all_user_transactions():
    users = database.get_all_users()
    user_transactions_list = []
    for user in users:
        transaction_list = get_user_pix_transactions(user.user_id)
        transaction_from_user = []
        for transaction in transaction_list:
            destination = transaction['to']['cnpj']
            if not destination:
                # using cpf because cnpj is not available in XP's openbanking api
                destination = transaction['to']['cpf']
            cnae_description = get_cnpj_cnaes_description(destination)
            transaction_from_user.append(
                Transaction(transaction['value'], ', '.join(cnae_description), transaction['date'])
            )
        user_transactions_list.append(UserTransactions(user.user_id, transaction_from_user))

    return user_transactions_list


def mock_user_transactions_list():
    result = [
        UserTransactions(
            "JOAO",
            [
                Transaction(100, "Educação infantil creche", "2022-01-01"),
                Transaction(50, "Fabricação outros brinquedos jogos recreativos especificados anteriormente",
                            "2022-01-02"),
                Transaction(200, "camisa flamenngo", "2022-01-03"),
                Transaction(20, "camisa flamego bebes", "2022-01-03"),
                Transaction(200, "gasolina", "2022-01-03"),
            ]
        ),
        UserTransactions(
            "MARIA",
            [
                Transaction(12, "Educação infantil pré-escola", "2022-01-01"),
                Transaction(80, "Comércio varejista brinquedos artigos recreativos", "2022-01-02"),
                Transaction(30, "brinquedos bebes", "2022-01-05"),
                Transaction(30, "leite", "2022-01-08"),
                Transaction(50, "comida", "2022-01-010"),
            ]
        ),
        UserTransactions(
            "ROBSON",
            [
                Transaction(60, "comida", "2022-01-01", 10),
                Transaction(300, "Aluguel aparelhos jogos eletrônicos", "2022-01-02", 15),
                Transaction(500, "skin fortnite", "2022-01-05", 12),
                Transaction(300, "controle xbola", "2022-01-08", 15),
                Transaction(50, "comida", "2022-01-010", 10),
            ]
        ),
        UserTransactions(
            "RODRIGO",
            [
                Transaction(60, "comida", "2022-01-01", 10),
                Transaction(40, "Exploração jogos eletrônicos recreativos", "2022-01-02", 15),
                Transaction(500, "camisa botafogo", "2022-01-05", 8),
                Transaction(300, "controle xbola", "2022-01-08", 15),
                Transaction(50, "nerd", "2022-01-010", 13),
            ]
        ),
    ]
    return result
