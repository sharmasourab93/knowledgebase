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
    
    config.add_route('create', '/create')
    config.add_route('get', '/one')
    config.add_route('get_id', '/item')
    config.add_route('update', 'update/{first}/{second}')
    config.add_route('delete', '/delete')
    config.add_route('list-all', '/')
    
    config.scan('.views')
    
    return config.make_wsgi_app()
