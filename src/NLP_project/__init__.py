import os
import sys
import logging

logging_str='[%(asctime)s - %(levelname)s - %(message)s]'
logs='logs'

logs_path=os.path.join(logs,'standings.logs.log')

os.makedirs(logs,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[logging.FileHandler(logs_path),
              logging.StreamHandler(sys.stdout)]

)
logger=logging.getLogger('NLP_project')