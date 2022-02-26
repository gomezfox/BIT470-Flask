""" Flask configuration """
from os import environ, path
import dotenv
import src.const
import sqlalchemy
from const import DB_DIRECTORY, DB_NAME

# enable retrieving secrets from environment
basedir = path.abspath(path.dirname(__file__))
dotenv.load_dotenv(path.join(basedir, '.env'))


# Base config
class Config:
    # Controls flask debug output
    TESTING = False
    DEBUG = False

    # TODO (per user) should export SECRET_KEY in .env file and use "environ.get('secret key')" below
    SECRET_KEY = 'f04af2af45d3a4e161a7dd2d17fdad414'

    # SQLITE
    DB_NAME = src.const.DB_NAME
    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/manthantrivedi/Documents/Bacancy/bacancy_blogs/flask_auth/myflaskproject/bookstore.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # JSONify
    JSONIFY_PRETTYPRINT_REGULAR = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+DB_DIRECTORY+DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
