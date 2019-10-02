from pyramid.view import view_config

from transaction import manager

from .models import DBSession
from .models import DictionaryCombo as Page

from .eng_dictionary import Dictionary as Parser
from sqlalchemy.orm.exc import NoResultFound


class Views(object):
   
    def __init__(self, request):
        self.request = request
    
    @view_config(route_name='create', renderer='json')
    def create_word(self):
        """
            To create an object,
            look up the meaning of the word on
            Cambridge university site & then
            insert both the word & meaning into
            the database.
            Eventually, returns word & meaning.
        """
        
        word = self.request.params.get('word', 'None')
        
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
        
    @view_config(route_name='get', renderer='json')
    def get_one(self):
        """
           To return values from the database
           based on values equalling word.
        """
        
        item = self.request.params.get('word', 'No word provided')
        
        try:
            
            page = DBSession.query(Page).filter_by(word=item).one()
            
            return dict(word=page.word, meaning=page.meaning)
        
        except NoResultFound:
            
            return dict(word=item, meaning='Not in db')
    
    @view_config(route_name='get_id', renderer='json')
    def get_id(self):
        """
            To return values from the database
            based on values equalling id.
        """
        # Adding item as 1 in the params
        # In view of the unittest cases
        item = self.request.params.get('item', 1)
        
        try:
            
            page = DBSession.query(Page).filter_by(uid=item).one()
            
            return dict(uid=page.uid, word=page.word, meaning=page.meaning)
        
        except NoResultFound:
            
            return dict(id=item, error="No value found")
        
    @view_config(route_name='update',  renderer='json',
                 permission='POST')
    def update(self):
        """
            To return an updated meaning
            to a word existing in the dictionary.
        """
        
        first = self.request.params.get('first', 'None')
        second = self.request.params.get('second', 'None')
        
        try:
            
            page = DBSession.query(Page).filter_by(word=first).first()
            page.meaning = second
        
            with manager:
                DBSession.add(page)
            
            manager.commit()
            
            return dict(word=first, meaning=second)
        
        except NoResultFound:
            
            return dict(word=first, error="Doesn't exist")
        
    @view_config(route_name='list-all',  renderer='json')
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
            
            to_delete = self.request.params.get('word', 'None')
            page = DBSession.query(Page).filter_by(word=to_delete).one()
            
            with manager:
                DBSession.delete(page)
            
            manager.commit()
            
        except NoResultFound:
            
            pass
        
        return self.list_all()
