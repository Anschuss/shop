class Configuration(object):
    DEBUG = True
    SECRET_KEY = "e17a2b3aecd610830c3d0fbcd6c870a5"

    ### SQLALCHEMY ###
    SQLALCHEMY_DATABASE_URI = "postgres+psycopg2://admin:1445@0.0.0.0:5432/shop"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

