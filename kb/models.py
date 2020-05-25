from pyramid.security import Allow, Everyone

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy.datamanager import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker
                           (extension=ZopeTransactionExtension())
                           )

Base = declarative_base()
metadata = MetaData()


class DictionaryCombo(Base):
    
    __tablename__ = 'dict'
    
    uid = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, unique=True, nullable=False)
    meaning = Column(Text)


class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),
    ]
    
    def __init__(self, request):
        pass
