from os import path

ENV = 'development'
SALT = 'cascadia'
DB_USERS = [('adam', 'a1234'), ('jason', 'j1234'), ('sean', 's1234'), ('steve', 't1234')]
APP_PATH = path.abspath(path.dirname(path.dirname(__file__)))  # parent folder of current file

# DATABASE
# database folder is project root folder parent folder of this file
DB_FOLDER = path.abspath(path.dirname(path.dirname(__file__))) + "/database"

DB_NAME = 'nftgram.db'
DB_FILE = DB_FOLDER + "/" + DB_NAME
