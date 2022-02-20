import os

from dotenv import load_dotenv
from flask import Flask
from .data import database

load_dotenv()
app = Flask(__name__)
app.secret_key = 'development key'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
VERSION = os.getenv('VERSION', '0.0.1')


if __name__ == '__main__':
    database.create_tables()
    app.run(port=6969)
