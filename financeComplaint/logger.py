import logging
from datetime import datetime
import os

ROOT_DIR= os.getcwd()
LOG_DIR="finance_logs"
os.makedirs(LOG_DIR, exist_ok=True)
CURRENT_TIME_STAMP= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
LOGNAME=f"finance_{CURRENT_TIME_STAMP}.log"
FULLPATH=os.path.join(ROOT_DIR,LOG_DIR,LOGNAME)

logging.basicConfig(filename=FULLPATH,
                    filemode="a+",
                    level=logging.INFO,
                    format="[%(asctime)s] %(lineno)d  %(name)s - %(levelname)s - %(message)s" )