import os
from tj_kits_wind.tj_logger.LoggerFactory import *

pwd = os.path.abspath(".")
logger_path = os.path.join(pwd, "logs")

logger_console = logger_console("wordy")
logger_file = logger_auto(name="logger_file", log_path=logger_path, logger_format="very_short")

logger_console.error("What dose the fox say ~")
logger_file.info("jijijijijijiji ,,, jijijijijijiji")
