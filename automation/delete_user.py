from rich.console import Console
from rich.prompt import Prompt
import os
import shutil

# 2. Handle deleted user. Move user2 docs to temp folder, so effectively delete user and maintain record of their docs.
console = Console()
prompt = Prompt()


def delete_user(user_folder, file):
  os.makedirs("temp_folder", exist_ok=True)
  shutil.movie(f'{user_folder}/{file}', "temp_folder")

if __name__ == "__main__":
  user_folder = Prompt.ask("Enter folder name to be deleted.")
  file = Prompt.ask("Enter file name to be moved.")
  if os.path.exists(f'{user_folder}/{file}'):
    delete_user(user_folder, file)
    console.print(f"The user's documents l'{file}' have been moved to the temporary folder")
  else:
    console.print("File does not exist.")