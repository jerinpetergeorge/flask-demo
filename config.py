def get_mysql_db_uri_from_env():
    import os
    user = os.environ.get('MYSQL_USER', 'root')
    password = os.environ.get('MYSQL_PASSWORD', 'password')
    host = os.environ.get('MYSQL_HOST', 'localhost')
    port = os.environ.get('MYSQL_PORT', '5432')
    db_name = os.environ.get('MYSQL_DB_NAME', 'my_simple_db')
    return 'mysql://{user}:{password}@{host}:{port}/{db_name}'.format(
        user=user,
        password=password,
        host=host,
        port=port,
        db_name=db_name
    )


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    SQLALCHEMY_DATABASE_URI = get_mysql_db_uri_from_env()


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'v#l70zX7ggfEsW!'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
