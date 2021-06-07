import logging
import logging.config
from configs.log import LOGGING
logging.config.dictConfig(LOGGING)

# load the logger here