from flask_restful import Resource, reqparse
from rest.api import db
from models.models import Student, Statement
from rest.schemas import StatementSchema

parser = reqparse.RequestParser()
parser.add_argument('all', type=bool)
parser.add_argument('title', type=str)
parser.add_argument('id', type=int)
parser.add_argument('title', type=str)
parser.add_argument('date', type=str)
parser.add_argument('students', action='append', type=int)


class Statements(Resource):
	def get(self):
		args = parser.parse_args()
		if args['all']:
			statements = Statement.query.all()
			statements_schema = StatementSchema()
			res = statements_schema.dump(statements, many=True)
		if args['title']:
			statements = Statement.query.filter(Statement.title == args['title']).all()
			statements_schema = StatementSchema()
			res = statements_schema.dump(statements, many=True)
		if args['id']:
			statement = Statement.query.get(args['id'])
			statement_schema = StatementSchema()
			res = statement_schema.dump(statement)
		return res, 200

	def post(self):
		args = parser.parse_args()
		statement = Statement(title=args['title'], date=args['date'])
		if args['students']:
			for student_id in args['students']:
				student = Student.query.get(student_id)
				if statement:
					statement.students.append(student)
		db.session.add(statement)
		db.session.commit()
		return 201

	def put(self):
		args = parser.parse_args()
		statement = Statement.query.get(args['id'])
		if args['title']:
			statement.title = args['title']
		if args['date']:
			statement.date = args['date']
		if args['students']:
			statement.students = []
			for student_id in args['students']:
				student = Student.query.get(student_id)
				statement.students.append(student)
		db.session.add(statement)
		db.session.commit()
		return 200

	def delete(self):
		args = parser.parse_args()
		statement = Statement.query.get(args['id'])
		db.session.delete(statement)
		db.session.commit()
		return 200
