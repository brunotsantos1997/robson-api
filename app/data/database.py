import sqlite3

from flask import g

from app.app import app
from .model import Objective, User

DATABASE = "data.db"


def create_tables():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id integer primary key,
                                    name text,
                                    email text
                                  )'''
                       )

        cursor.execute('''CREATE TABLE IF NOT EXISTS objectives (
                                    id integer primary key,
                                    user_id integer, 
                                    name text, 
                                    initial_date text,
                                    final_date text,
                                    initial_investment text, 
                                    recurring_investment text, 
                                    goal_value text,
                                    foreign KEY(user_id) REFERENCES users(id)
                                  )'''
                       )

        db.commit()
        db.close()


def add_objective(objective: Objective):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        command = f"""INSERT INTO objectives VALUES (null,
                        '{objective.user_id}',
                        '{objective.name}',
                        '{objective.initial_date}',
                        '{objective.final_date}',
                        '{objective.initial_investment}',
                        '{objective.recurring_investment}',
                        '{objective.goal_value}')"""

        cursor.execute(command)
        db.commit()
        db.close()


def update_objective(objective: Objective):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        command = f"""UPDATE objectives SET 
                        name = '{objective.name}',
                        initial_date = '{objective.initial_date}',
                        final_date = '{objective.final_date}',
                        initial_investment = '{objective.initial_investment}',
                        recurring_investment = '{objective.recurring_investment}',
                        goal_value = '{objective.goal_value}'
                        WHERE id = '{objective.id}'"""

        cursor.execute(command)
        db.commit()
        db.close()


def add_user(users: User):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        command = f"""INSERT INTO users VALUES (null, '{users.name}', '{users.email}')"""

        cursor.execute(command)
        db.commit()
        db.close()


def update_user(user: User):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        command = f"""UPDATE users SET 
                        name = '{user.name}',
                        email = '{user.email}'
                        WHERE id = '{user.user_id}'"""

        cursor.execute(command)
        db.commit()
        db.close()
        return cursor.rowcount > 0


def get_user(user_id):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        command = f"""SELECT * FROM users WHERE id = '{user_id}'"""
        cursor.execute(command)
        user = cursor.fetchone()
        db.close()
        if user is None:
            raise FileNotFoundError
        return User(user[0], user[1], user[2])


def delete_user(user_id):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        command = f"""DELETE FROM users WHERE id = '{user_id}'"""
        cursor.execute(command)
        db.commit()
        db.close()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
