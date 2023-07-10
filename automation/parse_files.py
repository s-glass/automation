from rich.console import Console
from rich.prompt import Prompt
import os

# 4. Parse log file for errors and warnings. Parse log file in logs folder for errors and warnings AND create two separate log files in a target directory: errors.log with all error messages and warnings.log with all warning messages.

console = Console()
prompt = Prompt()

def parse_files(log_file_path, target_directory):
  log_file_path = input("Enter the path to the log file: ")
  target_directory = input("Enter the path to the target directory: ")
  errors_file_path = os.path.join(target_directory, 'errors.log')
  warnings_file_path = os.path.join(target_directory, 'warnings.log')
  errors_file = open(errors_file_path, 'w')
  warnings_file = open(warnings_file_path, 'w')


  with open(log_file_path) as log_file:
    for line in log_file:
        if 'ERROR' in line.lower():
            errors_file.write(line)
        elif 'WARNING' in line.lower():
            warnings_file.write(line)

  errors_file.close()
  warnings_file.close()

  print("Log file parsed successfully!")

if __name__ == "__main__":
  log_file_path = Prompt.ask("Enter file path for message log")
  if os.path.exists(log_file_path):
     parse_files(log_file_path, "logs")
  else:
     console.print(f"File does not exist")