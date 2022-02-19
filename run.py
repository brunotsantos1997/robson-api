from flask.cli import FlaskGroup

from app import app, database


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    database.create_tables()


if __name__ == "__main__":
    database.create_tables()
    cli()
