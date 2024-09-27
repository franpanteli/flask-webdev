# Coppied into this file from app.py
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# basedir = os.path.abspath(os.path.dirname(__file__))

#     #a secret key for creating forms
# app.config['SECRET_KEY'] = "keep it a secret, at all costs"

#     #SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     f'sqlite:///{os.path.join(basedir, "data-dev.sqlite")}'

#         #to supress a warning when doing this
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#After adding classes into this
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "keep it a secret, at all costs"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data-dev.sqlite")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def init_app(app):
    pass

config = {'default': Config}
