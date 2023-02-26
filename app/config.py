import os
from app.DbConnection import DbConnection


basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
DB = DbConnection()
