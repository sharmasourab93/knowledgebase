from pyramid.view import view_config

#TODO: Do Not Use transaction
from transaction import manager

from .models import DBSession
from .models import DictionaryCombo as Page

from .eng_dictionary import Dictionary as Parser
from sqlalchemy.orm.exc import NoResultFound


class Views(object):
   
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name='create', renderer='json')
    def create_word(self, word=None):
        """
            To create an object,
            look up the meaning of the word on
            Cambridge university site & then
            insert both the word & meaning into
            the database.
            Eventually, returns word & meaning.
        """
        if word is None:
            word = self.request.matchdict['word']
        
        try:
            page = DBSession.query(Page).filter_by(word=word).one()
            
            return dict(word=page.word, meaning=page.meaning)
        
        except NoResultFound:
        
            meaning = Parser(word)
            meaning = meaning.lookup_browse()
    
            if meaning is None:
        
                return dict(word=word, meaning=meaning)
    
            else:
                
                inject = Page(word=word, meaning=meaning)
        
                with manager:
                    DBSession.add(inject)
        
                manager.commit()
        
                return dict(word=word, meaning=meaning)
        
    @view_config(route_name='get_one', renderer='json')
    def get_one(self, word=None):
        """
           To return values from the database
           based on values equalling word.
        """
        
        if word is None:
            word = self.request.matchdict['word']
        
        try:
            
            page = DBSession.query(Page).filter_by(word=word).one()
            
            return dict(word=page.word, meaning=page.meaning)
        
        except NoResultFound:
            
            return dict(word=word, meaning='Not in db')
    
    @view_config(route_name='get_id', renderer='json')
    def get_id(self, id=None):
        """
            To return values from the database
            based on values equalling id.
        """
        
        if id is None:
            id = self.request.matchdict['id']
        
        try:
            
            page = DBSession.query(Page).filter_by(uid=id).one()
            
            return dict(uid=page.uid, word=page.word, meaning=page.meaning)
        
        except NoResultFound:
            
            return dict(id=id, error="No value found")
        
    @view_config(route_name='update',  renderer='json')
    def update(self, first=None, second=None):
        """
            To return an updated meaning
            to a word existing in the dictionary.
        """
        
        if first is None and second is None:
            first = self.request.matchdict['first']
            second = self.request.matchdict['second']
        
        try:
            
            page = DBSession.query(Page).filter_by(word=first).one()
            page.meaning = second
        
            with manager:
                DBSession.add(page)
            
            manager.commit()
            
            return dict(word=first, meaning=second)
        
        except NoResultFound:
            
            return dict(word=first, meaning="Doesn't exist")
        
    @view_config(route_name='list',  renderer='json',
                 request_method='GET')
    def list_all(self):
        """
            List all the words and their
            meanings  in dictionary table.
        """
    
        pages = DBSession.query(Page).order_by(Page.word).all()
        
        dict_word = {i.word: [i.meaning, i.uid] for i in pages}
        
        return dict_word
    
    @view_config(route_name='delete',  renderer='json')
    def delete(self):
        """
             To delete a word from db
             and return all the words & meanings
             after deletion
        """
        try:
            
            to_delete = self.request.matchdict['word']
            page = DBSession.query(Page).filter_by(word=to_delete).one()
            
            with manager:
                DBSession.delete(page)
            
            manager.commit()
            
        except NoResultFound:
            
            pass
        
        return self.list_all()
