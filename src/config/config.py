class Config:
    DEBUG = True
    # Swagger
    RESTX_MASK_SWAGGER = True


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = "prod"


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)
