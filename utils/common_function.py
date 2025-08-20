import os
import pandas as pd
from utils.logger import get_logger
from utils.custom_exception import CustomException
import yaml
import numpy as np
import pandas as pd
import time
import sys
import pandas as pd

logger = get_logger(__name__)

def read_yalm_file(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("=========================================================")
            logger.info("YAML file read successfully.")
            return config
    except Exception as e:
        logger.error("Error occurred while reading the YAML file.")
        raise CustomException("Custom exception in read_yaml_file", e)

    
    
def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

    # yield pd.DataFrame(
    #     np.random.randn(5, 10),
    #     columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    # )

    # for word in text.split(" "):
    #     yield word + " "
    #     time.sleep(0.02)