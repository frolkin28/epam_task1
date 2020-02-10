from flask_restful import Resource, reqparse
from rest.api import db
from models.models import Student_mark
from rest.schemas import MarkSchema

parser = reqparse.RequestParser()
parser.add_argument('subject', type=str)
parser.add_argument('mark', type=int)
parser.add_argument('student', type=int)
parser.add_argument('id', type=int)


class Marks(Resource):
	def get(self):
		args = parser.parse_args()
		if args['subject']:
			marks = Student_mark.query.filter(
				Student_mark.subject == args['subject']).all()
			marks_schema = MarkSchema()
			res = marks_schema.dump(marks, many=True)
		return res, 200

	def post(self):
		args = parser.parse_args()
		mark = Student_mark(mark=args['mark'], subject=args['subject'], student_id=args['student'])
		db.session.add(mark)
		db.session.commit()
		return 201

	def put(self):
		args = parser.parse_args()
		mark = Student_mark.query.get(args['id'])
		if args['mark']:
			mark.mark = args['mark']
		db.session.add(mark)
		db.session.commit()
		return 200

	def delete(self):
		args = parser.parse_args()
		mark = Student_mark.query.get(args['id'])
		db.session.delete(mark)
		db.session.commit()
		return 200