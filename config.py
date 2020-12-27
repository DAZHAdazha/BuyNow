import os
DEBUG = True
# config database URL here
# format: dialect+driver://username:password@host:port/database

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# whether open dynamic modification, if it is on, server performance will be curtailed, and this API will be abandoned, thus False is recommended
SQLALCHEMY_TRACK_MODIFICATIONS = False 
# SECRET_KEY
# SQLALCHEMY_DB