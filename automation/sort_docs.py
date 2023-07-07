from rich.console import Console
from rich.prompt import Prompt
import os
import shutil

# 3. Sort docs to appropriate folders. Go through given folder and sort docs into additional folders based on file type. Move log files into logs folder and email files into mail folder - create them if they don't already exist. 

console = Console()
prompt = Prompt()

def sort_docs(folder_to_sort):

  logs_folder = os.path.join(folder_to_sort, 'logs')
  if not os.path.exists(logs_folder):
      os.makedirs(logs_folder)

  mail_folder = os.path.join(folder_to_sort, 'mail')
  if not os.path.exists(mail_folder):
      os.makedirs(mail_folder)

  for file_name in os.listdir(folder_to_sort):
      file_path = os.path.join(folder_to_sort, file_name)
      if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension == '.txt':
            shutil.move(file_path, logs_folder)
        elif file_extension == '.mail':
            shutil.move(file_path, mail_folder)


if __name__ == "__main__":
    folder_to_sort = Prompt.ask("Enter folder to sort")
    sort_docs(folder_to_sort)
    console.print("Documents sorted successfully!")
