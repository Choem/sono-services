from sqlalchemy import Column, String, Integer

from .base import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return "<User(id='{0}', username='{1}', email='{2}')>".format(self.id, self.username, self.email)