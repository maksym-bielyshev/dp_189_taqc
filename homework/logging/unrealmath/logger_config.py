logger_settings = {
    "version": 1,
    "formatters": {
        "default_formatter": {
            "format": "%(asctime)s - %(name)s - %(message)s"
        },
    },
    "handlers": {
        "addition": {
            "class": "logging.FileHandler",
            "formatter": "default_formatter",
            "filename": "addition.log"
        },
        "subtraction": {
            "class": "logging.FileHandler",
            "formatter": "default_formatter",
            "filename": "subtraction.log"
        },
    },
    "loggers": {
        "unrealmath.addition": {
            "handlers": ["addition"],
            "level": "INFO"
        },
        "unrealmath.subtraction": {
            "handlers": ["subtraction"],
            "level": "INFO"
        },
    },
}
