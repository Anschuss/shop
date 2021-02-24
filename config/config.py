class Configuration(object):
    DEBUG = True
    SECRET_KEY = "e17a2b3aecd610830c3d0fbcd6c870a5"

    ### SQLALCHEMY ###
    SQLALCHEMY_DATABASE_URI = "postgres+psycopg2://admin:1445@0.0.0.0:5432/shop"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### CELERY ###

    CELERY_BROKER_URL = "redis://0.0.0.0:6379/0"
    CELERY_RESULT_BACKEND = "redis://0.0.0.0:6379/1"
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_TASK_SERIALIZER = "json"
    CELERY_RESULT_SERIALIZER = "json"

