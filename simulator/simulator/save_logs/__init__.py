import os
from datetime import datetime
from typing import List
from constants import GAME_TYPE

class SaveLogs:
    '''
    Abstract class to save logs
    '''

    def __init__(self, path) -> None:
        self.path = os.path.join(path, str(datetime.now().strftime('%s') + self.EXTENTION))

    def save_logs(self, logs: List[List[GAME_TYPE]]) -> None:
        pass # This function must be overrided by all implementing classes

