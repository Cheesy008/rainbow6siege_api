logger_config = {
    'version': 1,
    'formatters': {
        'std_formatter': {
            'format': '{levelname} - {name} - {message}',
            'style': '{',
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'ERROR',
                'formatter': 'std_formatter',
            }
        },
        'loggers': {
            'operators_logger': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            }
        }
    }
}