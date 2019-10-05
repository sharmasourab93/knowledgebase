from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, RootFactory, Base


def main(global_config, **settings):
    
    engine = engine_from_config(settings, 'sqlalchemy.')
    
    DBSession.configure(bind=engine)
    
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    config = Configurator(settings=settings,
                          root_factory=RootFactory)
    
    config.add_route('create', r'/create/{word}')
    config.add_route('get_one', r'/get/{word}')
    config.add_route('get_id', r'/item/{id:\d+}')
    config.add_route('update', r'update/{first}/{second}')
    config.add_route('delete', r'/delete/{word}')
    config.add_route('list', r'/')
    
    config.scan('.views')
    
    return config.make_wsgi_app()
