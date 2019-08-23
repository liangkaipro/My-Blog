# encoding: utf-8

class Config(object):
    SECREY_KEY = '82e518c39571bd501ed126f62acaf1b6%'


class ProConfig(Config):
    pass


class DevCofig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root1234@localhost:3306/blog'
