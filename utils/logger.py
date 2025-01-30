import logging
import sys

from loguru import logger

"""


# log setting over view

## define of log level means

error  : ocurred expect to error
warning: Error caused by user
info   : user activity
debug  : develop

### log format

> error
{Time Stamp}:{Log level}: {Message} {file} {line}

> waring
{Time Stamp}:{Log level}: {Message} {warning_keys}

> info
{Time Stamp}:{Log level}: {Message}

> debug
{Time Stamp}:{Log level}: {Message}

### journal
Out put all log to file when environment is local.
To activate this feature, set the following variable to True in .env file.
- LOCAL_OUTPUT_TO_FILE=True

### note
- when raised log level is error
log message will be add file name and ocurred line number.

- debug log level only output in development and local environment.
"""


def init_logger(log_format: str):
    logger.remove()
    log_level = logging.DEBUG
    return logger.add(sys.stderr, format=log_format, level=log_level)


def log_error(message: str):
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level}: {message} - file name: {file} raised {line} line</level>"
    init_logger(log_format)
    logger.opt(depth=1).error(message)


def log_warning(message: str, warning_keys: list[str]):
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level}: {message} - warning keys: {extra[extra_value]}</level>"
    init_logger(log_format)
    logger.opt(depth=1).warning(message, extra_value=warning_keys)


def log_info(message: str):
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level} {message}</level>"
    )
    init_logger(log_format)
    logger.info(message)


def log_debug(message: str):
    log_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> <level>{level}: {message}</level>"
    )
    init_logger(log_format)
    logger.debug(message)


if __name__ == "__main__":
    log_error("test")
    log_warning("test", ["test", "test2"])
    log_info("test")
    # settings.FASTAPI_ENV = FastApiEnv.DEVELOPMENT
    log_debug("test")
    log_debug("test")
