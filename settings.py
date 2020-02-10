class Config:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:012810@localhost/epam_task'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SERVER_NAME = '127.0.0.1:5050'