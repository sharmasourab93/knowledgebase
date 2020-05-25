from setuptools import setup, find_packages


requires = [
    'transaction',
    'pyramid',
    'waitress',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'sqlalchemy',
    'psycopg2',
    'alembic',
    'zope.sqlalchemy',
    'webtest',
]

setup(
    name='kb',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = kb:main'
        ],
        
        'console_scripts': [
            'initialize_kb_db = kb.scripts.initialize_db:main'
            ],
    },
    include_package_data=True,
    packages=find_packages(),
)
