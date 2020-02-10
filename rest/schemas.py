from flask_marshmallow import Marshmallow
from models.models import Statement, Student, Student_mark

ma = Marshmallow()


class MarkSchema(ma.ModelSchema):
	class Meta:
		model = Student_mark


class StudentSchema(ma.ModelSchema):
	marks = ma.Nested(MarkSchema, many=True)

	class Meta:
		model = Student


class StatementSchema(ma.ModelSchema):
	students = ma.Nested(StudentSchema, many=True)

	class Meta:
		model = Statement
