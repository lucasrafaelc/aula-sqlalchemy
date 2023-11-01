from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///usuarios.db"

db = SQLAlchemy(app)

from views import rotas_usuario

app.register_blueprint(rotas_usuario, url_prefix='/api/')