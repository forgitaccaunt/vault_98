from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy import create_engine


sqlite_db = 'sqlite:///Databases/vault98.db'
engine = create_engine(sqlite_db)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    age = Column(Date)
    rank = Column(String)


class Journal(Base):
    __tablename__ = 'journal'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    note = Column(String)
    date = Column(Date)
    user = relationship(User)


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    info = Column(String)


class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    id_game = Column(Integer, ForeignKey('games.id'))
    id_user = Column(Integer, ForeignKey('users.id'))
    score = Column(Integer)
    game = relationship(Game)
    user = relationship(User)


class Userlogs(Base):
    __tablename__ = 'userlogs'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    note = Column(String)
    user = relationship(User)


Base.metadata.create_all(bind=engine)
