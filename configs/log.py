import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(process)d-%(thread)d:%(name)s:%(lineno)s] - [%(module)s:%(funcName)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.log',
            'formatter': 'standard',
            'maxBytes': 1048576, 
            'backupCount': 5
        },
        'test': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/test.log',
            'formatter': 'standard',
            'maxBytes': 1048576, 
            'backupCount': 5
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'test': {
            'handlers': ['file'], # keep test and app in one log
            'level': 'DEBUG',
            'propagate': True,
        },
        'database': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'models': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'app': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'controller': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'decorator': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'utils': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'dbmodels': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
