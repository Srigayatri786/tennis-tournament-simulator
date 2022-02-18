import os
import csv
from datetime import datetime

class SaveLogsAsCSV:
    def __init__(self, path):
        self.path = os.path.join(path, str(datetime.now().strftime('%s') + '.csv'))

    def save_logs(self, logs):
        with open(self.path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(logs)
