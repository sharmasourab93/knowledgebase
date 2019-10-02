"""
    Unittest cases for the following Views & Models:
        1. Views
            i. Creating a word
           ii. Getting one word
          iii. Getting one id
           iv. Updating a word
        
        2. Models
           i. Add or Delete word
"""
import unittest
import transaction
from pyramid import testing
from .models import DBSession, Base


def init_db():
    from sqlalchemy import create_engine
    
    engine = create_engine('postgresql://sourab:password' +
                           '@localhost:5432/mydb')
    
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    
    return DBSession


class ViewTest(unittest.TestCase):
    
    def setUp(self):
        self.session = init_db()
        self.session.expire_on_commit = False
        self.config = testing.setUp()
    
    def tearDown(self):
        self.session.remove()
        testing.tearDown()
    
    def test_create_word_view(self):
        from .views import Views
        
        request = testing.DummyRequest()
        view_obj = Views(request)
        
        # Passing None as an object by default
        data = view_obj.create_word()
        self.assertEqual(data['word'], 'None')
    
    def test_get_one_word(self):
        from .views import Views
        meaning = "Not in db"
        
        request = testing.DummyRequest()
        view_obj = Views(request)
        data = view_obj.get_one()
        
        self.assertEqual(data['meaning'], meaning)
        
    def test_get_one_id(self):
        from .views import Views
        
        request = testing.DummyRequest()
        view_obj = Views(request)
        data = view_obj.get_id()
        
        self.assertEqual(data['uid'], 1)
    
    def test_update_word(self):
        from .views import Views
        
        request = testing.DummyRequest()
        view_obj = Views(request)
        print(request)
        data = view_obj.update()
        print(data)
        self.assertEquals(data['word'], 'None')


class ModelsTest(unittest.TestCase):
    
    def setUp(self):
        self.session = init_db()
        self.config = testing.setUp()
    
    def tearDown(self):
        self.session.remove()
        testing.tearDown()
        
    def test_add_delete_word(self):
        from .models import DictionaryCombo
        from sqlalchemy.orm.exc import NoResultFound

        try:
            
            page = DBSession.query(DictionaryCombo)\
                .filter_by(word="joy").one()

            self.assertEqual(page.word, "joy")
            self.assertEqual(page.meaning, "happy")
            
        except NoResultFound:
            
            page = DictionaryCombo(word="joy", meaning="happy")
            
            with transaction.manager:
                DBSession.add(page)
                
            transaction.manager.commit()
            
            self.assertEqual(page.word, "joy")
            self.assertEqual(page.meaning, "happy")
        
        finally:
            page = DBSession.query(DictionaryCombo)\
                .filter_by(word="joy").one()
            
            with transaction.manager:
                DBSession.delete(page)
                
            transaction.manager.commit()
