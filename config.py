import os

class Config:
    QUOTE_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = '65897'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:54321@localhost/blog'
    
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config:The parent configuration class with general configuration settings
    ''' 
    DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')

config_options = {
'development':DevConfig,
'production':ProdConfig
}