import sqlite3

from model import Objective, Users


class DataBase:
    DATA = "data.db"

    def __init__(self):
        self._create_tables()

    def _create_tables(self):
        connection = sqlite3.connect(self.DATA)
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id integer primary key,
                                    name text,
                                    email text
                                  )'''
                       )

        # Create table
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

        # Save (commit) the changes
        connection.commit()
        connection.close()

    def add_objective(self, objective: Objective):
        connection = sqlite3.connect(self.DATA)
        cursor = connection.cursor()
        command = f"""INSERT INTO objectives VALUES (null,
                        '{objective.user_id}',
                        '{objective.name}',
                        '{objective.initial_date}',
                        '{objective.final_date}',
                        '{objective.initial_investment}',
                        '{objective.recurring_investment}',
                        '{objective.goal_value}')"""

        cursor.execute(command)
        connection.commit()
        connection.close()

    def add_users(self, users: Users):
        connection = sqlite3.connect(self.DATA)
        cursor = connection.cursor()
        command = f"""INSERT INTO users VALUES (null,
                        '{users.user_id}',
                        '{users.name}',
                        '{users.email}',)"""

        cursor.execute(command)
        connection.commit()
        connection.close()
