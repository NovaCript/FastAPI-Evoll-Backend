from loguru import logger
from core.config import settings


logger.add(
    settings.loger.log_path,
    format=settings.loger.format,
    level=settings.loger.level,
    rotation=settings.loger.rotation,
    retention=settings.loger.retention,
    compression=settings.loger.compression,
    serialize=settings.loger.serialize,
)


'''
ignore debug logs

to catching logs in json format
    do serialize=True and change format .log to .json
        ("log_core/logs_json/info.log")
            in core.config.LogConfig
            
use decorator @logger.catch
@logger.catch
def main() -> None:
    logger.debug("Hello, World!")
'''