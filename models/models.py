from rest.api import db

statements = db.Table('statements',
					  db.Column('statement_id', db.Integer, db.ForeignKey('statement.id')),
					  db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
					  )


class Statement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255))
	date = db.Column(db.Date)
	students = db.relationship('Student', secondary=statements, backref=db.backref('statements', lazy='dynamic'))


class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	marks = db.relationship('Student_mark', backref='student', lazy=True)
	group = db.Column(db.String(60), nullable=False)


class Student_mark(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subject = db.Column(db.String(255), nullable=False)
	mark = db.Column(db.Integer, nullable=False)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
