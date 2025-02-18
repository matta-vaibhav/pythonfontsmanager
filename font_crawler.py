import os
import subprocess
import re

class FontCrawlerManager:
    def __init__(self, command, log_file='logs.txt', pattern=r'.*\\DOWNLOADS\\FONTS*'):
        self.command = command
        self.log_file = log_file
        self.pattern = pattern
    
    def delete_log_file(self):
        """Deletes the log file if it exists."""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
            print(f"{self.log_file} has been deleted.")
    
    def execute_command(self):
        """Executes the command and redirects output to the log file."""
        with open(self.log_file, 'w') as log_file:
            # print("Executing Command : net stop FontCache")
            # subprocess.run("net stop FontCache", shell=True, stdout=log_file)

            # print("Executing Command : net start FontCache")
            # subprocess.run("net start FontCache", shell=True, stdout=log_file)

            subprocess.run(self.command, shell=True, stdout=log_file)
        print(f"Executed command: {self.command}")
    
    def count_matching_lines(self):
        """Counts the number of lines in the log file matching the given pattern."""
        line_count = 0
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                for line in file:
                    if re.search(self.pattern, line):
                        line_count += 1
        return line_count

    def run(self):
        """Combines the steps: deletes log file, executes command, and counts matching lines."""
        self.delete_log_file()
        self.execute_command()
        matching_lines = self.count_matching_lines()
        return matching_lines

