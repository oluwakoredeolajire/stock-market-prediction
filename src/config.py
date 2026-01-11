import os
import numpy as np

#Path configurations
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Dataset configurations
DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'AAME.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed')

#Model configurations
TARGET_COLUMN = 'Close'

#Training configurations
RANDOM_STATE = 42
TEST_SIZE = 0.2