# encoding: utf-8

class Config(object):
    pass


class ProConfig(Config):
    pass


class DevCofig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root1234@localhost:3306/blog'
