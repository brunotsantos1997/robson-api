from flask import request, Response

from app import app, database, Objective


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
