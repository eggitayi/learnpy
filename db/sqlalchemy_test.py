from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/py')
DBSession = sessionmaker(bind=engine)

class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	books = relationship('Book')


class Book(Base):
	__tablename__ = 'book'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	user_id = Column(String(20), ForeignKey('user.id'))



def addUser(new_user):
	session = DBSession()
	session.add(new_user)
	session.commit()
	session.close()

def getUserById(user_id):
	session = DBSession()
	user = session.query(User).filter(User.id==user_id).one()
	session.close()
	return user

def getAllUsers():
	session = DBSession()
	users = session.query(User)
	session.close()
	return users

def getBookById(book_id):
	session = DBSession()
	book = session.query(Book).filter(Book.id==book_id).one()
	session.close()
	return book

users = getAllUsers()
for u in users:
	print u.id, u.name
	for b in u.books:
		print b.name

book_java = getBookById('1')
print book_java.id, book_java.name, book_java.user_id
