from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

api = Api(app)
migrate = Migrate(app, db)

from rest.statements import Statements
from rest.students import Students
from rest.marks import Marks

api.add_resource(Statements, '/statement')
api.add_resource(Students, '/student')
api.add_resource(Marks, '/mark')
