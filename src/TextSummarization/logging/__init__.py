import logging
import os
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(message)s]"
log_dir = "logs"
log_filpath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
                    level=logging.INFO, 
                    format=logging_str,
                    handlers=
                    [logging.FileHandler(log_filpath), 
                    logging.StreamHandler(sys.stdout)]

)

logger = logging.getLogger("TextSummarizationLogger")