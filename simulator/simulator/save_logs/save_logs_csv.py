import csv
from simulator.save_logs import SaveLogs

class SaveLogsAsCSV(SaveLogs):
    """Save the logs as a CSV"""

    EXTENTION: str = '.csv'

    def save_logs(self, logs):
        """Saves logs in a CSV file"""
        with open(self.path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(logs)
