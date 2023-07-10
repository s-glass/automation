from rich.console import Console
from rich.prompt import Prompt
import os
import sys
from automation.create_folder import create_folder
from automation.delete_user import delete_user
from automation.sort_docs import sort_docs
from automation.parse_files import parse_files

# 5. Create a menu-driven application. give user a list 1-4 of automation tasks and let them choose one. Customize app by incorporating an addiitonal automation task. Choose one: counting number of specific file types. 

console = Console()
prompt = Prompt()


def count_file_types(file_extension, directory):
    file_types = {}
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_extension = os.path.splitext(file_name)[1].lower()
            if file_extension in file_types:
                file_types[file_extension] += 1
            else:
                file_types[file_extension] = 1
        console.print(f"There are {file_types}{file_extension} files.")
        return file_types


def menu_tasks():
  print("Select one of these Automation Tasks:")
  print("1. Count the number of specific file types in a directory.")
  print("2. Create a new folder with a specified name.")
  print("3. Handle deleted user.")
  print("4. Sort documents to appropriate folders by file type.")
  print("5. Parse log files for errors and warnings.")
  choice = input("Enter your choice (1-5): ")

  if choice == '1':
        directory = input("Enter the path to the directory: ")
        file_types = count_file_types(directory)
        print("File Types:")
        for file_type, count in file_types.items():
            print(f"{file_type}: {count}")
  elif choice == '2':
        folder_name = Prompt.ask("Enter a name for the folder to create")
        create_folder(folder_name)
  elif choice == '3':
        user_folder = Prompt.ask("Enter folder name to be deleted")
        delete_user(user_folder)
  elif choice == '4':
        folder_to_sort = Prompt.ask("Enter folder to sort")
        sort_docs(folder_to_sort)
  elif choice == '5':
        log_file_path = Prompt.ask("Enter the path to the log file: ")
        parse_files(log_file_path, "logs")
  else:
      print("Invalid choice. Please select a valid option.")


def exit_message(message):
     sys.exit(message)

if __name__ == "__main__":
      try:
           menu_tasks()
      except KeyboardInterrupt:
            exit_message("Exiting Menu")
