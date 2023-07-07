from rich.console import Console
from rich.prompt import Prompt
import os

console = Console()
prompt = Prompt()

# 1. Create new folder with specified name

def create_folder(folder_name):
    try:
      os.mkdir(folder_name)
      console.print(f"Folder '{folder_name}' successfully created")
    except FileExistsError:
      console.print(f"Folder '{folder_name}' already exists.")


if __name__ == "__main__":
    folder_name = Prompt.ask("Enter a name for the folder to create")
    create_folder(folder_name)
