from flask_restful import Resource, reqparse
from rest.api import db
from models.models import Student
from rest.schemas import StudentSchema

parser = reqparse.RequestParser()
parser.add_argument('all', type=bool)
parser.add_argument('id', type=int)
parser.add_argument('name', type=str)
parser.add_argument('group', type=str)


class Students(Resource):
	def get(self):
		args = parser.parse_args()
		if args['all']:
			students = Student.query.all()
			students_schema = StudentSchema()
			res = students_schema.dump(students, many=True)
		if args['name']:
			statements = Student.query.filter(Student.name == args['name']).all()
			statements_schema = StudentSchema()
			res = statements_schema.dump(statements, many=True)
		if args['id']:
			statement = Student.query.get(args['id'])
			statement_schema = StudentSchema()
			res = statement_schema.dump(statement)
		return res, 200

	def post(self):
		args = parser.parse_args()
		student = Student(name=args['name'], group=args['group'])
		db.session.add(student)
		db.session.commit()
		return 201

	def put(self):
		args = parser.parse_args()
		student = Student.query.get(args['id'])
		if args['name']:
			student.name = args['name']
		if args['group']:
			student.group = args['group']
		db.session.add(student)
		db.session.commit()
		return 200

	def delete(self):
		args = parser.parse_args()
		student = Student.query.get(args['id'])
		for mark in student.marks:
			db.session.delete(mark)
			db.session.commit()
		db.session.delete(student)
		db.session.commit()
		return 200

