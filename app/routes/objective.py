from flask import request, Response

from app import app, database, Objective
from app.ai.transactions import generate_clusters
from app.data.model import UserTransactions, Transaction


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


@app.route("/ai/cluster/")
def clusterize_users():
    user_transactions_list = [
        UserTransactions(
            "JOAO",
            [
                Transaction(100, "Educação infantil creche", "2022-01-01", 1),
                Transaction(50, "Fabricação outros brinquedos jogos recreativos especificados anteriormente", "2022-01-02", 2),
                Transaction(200, "camisa flamengo", "2022-01-03", 8),
                Transaction(20, "camisa flamengo bebes", "2022-01-03", 4),
                Transaction(200, "gasolina", "2022-01-03", 5),
            ]
        ),
        UserTransactions(
            "MARIA",
            [
                Transaction(12, "Educação infantil pré-escola", "2022-01-01", 1),
                Transaction(80, "Comércio varejista brinquedos artigos recreativos", "2022-01-02", 2),
                Transaction(30, "brinquedos bebes", "2022-01-05", 4),
                Transaction(30, "leite", "2022-01-08", 6),
                Transaction(50, "comida", "2022-01-010", 10),
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

    return f'{generate_clusters(user_transactions_list, 2)}'
