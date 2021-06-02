from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.dev.env'
load_dotenv(dotenv_path=env_path)
# load_dotenv() # load env vars before loading any modules
import logging
import logging.config
from configs.log import LOGGING
logging.config.dictConfig(LOGGING)
#logger = 'processor' if os.getenv('ENVIRONMENT') != 'TEST' else 'test'
logger = logging.getLogger('app')
from configs.db import db_conn

class App:

    def __init__(self) -> None:
        self.dbconn = db_conn()
        print("App is initialized")


if __name__ == '__main__':
    print("app is called")
    app = App()


