import pytest
import os
import sys
from rich.prompt import Prompt
from rich.console import Console
from automation.create_folder import create_folder
from automation.delete_user import delete_user
from automation.sort_docs import sort_docs
from automation.parse_files import parse_files
from automation.menu_tasks import count_file_types, menu_tasks, exit_message


def test_automation():
    assert True


## Testing for create_folder

def test_create_folder(monkeypatch):
    folder_name = "test_folder"

    # Mock user input for the prompt
    monkeypatch.setattr("builtins.input", lambda _: folder_name)

    # Execute the create_folder function
    create_folder(folder_name)

    # Check if the folder was created and the expected message was printed
    assert os.path.exists(folder_name)
    captured = capsys.readouterr()
    assert f"Folder '{folder_name}' successfully created" in captured.out


## Testing for delete_user

def test_delete_user(monkeypatch, capsys):
    user_folder = "test_folder"
    file = "test_file.txt"

    # Create a file in the user_folder
    os.makedirs(user_folder, exist_ok=True)
    open(f'{user_folder}/{file}', 'w').close()

    # Mock user input for the prompts
    monkeypatch.setattr("builtins.input", lambda _: user_folder)

    # Execute the delete_user function
    delete_user(user_folder, file)

    # Check if the file was moved and the expected message was printed
    assert not os.path.exists(f'{user_folder}/{file}')
    captured = capsys.readouterr()
    assert f"The user's document '{file}' has been moved to the temporary folder" in captured.out


## Testing for parse_files

def test_parse_files(monkeypatch, tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "test.log"
    log_file.write_text("Line 1\nLine 2\nWARNING: This is a warning message.\nERROR: This is an error message.")

    # Set up user inputs for the prompt
    monkeypatch.setattr("builtins.input", lambda prompt: str(log_file) if "log file" in prompt else str(tmp_path))

    # Execute the parse_files function
    parse_files(None, None)

    # Check if the error and warning files were created and contain the expected content
    errors_file_path = tmp_path / "errors.log"
    warnings_file_path = tmp_path / "warnings.log"
    assert errors_file_path.exists()
    assert warnings_file_path.exists()
    assert errors_file_path.read_text() == "ERROR: This is an error message."
    assert warnings_file_path.read_text() == "WARNING: This is a warning message."

    # Clean up the temporary files
    errors_file_path.unlink()
    warnings_file_path.unlink()


## Testing for sort_docs

def test_sort_docs(monkeypatch, tmp_path):
    # Create a temporary folder with files
    folder_to_sort = tmp_path / "test_folder"
    folder_to_sort.mkdir()
    (folder_to_sort / "file1.txt").write_text("This is a log file.")
    (folder_to_sort / "file2.mail").write_text("This is a mail file.")
    (folder_to_sort / "file3.txt").write_text("This is another log file.")
    (folder_to_sort / "file4.txt").write_text("This is a third log file.")

    # Execute the sort_docs function
    sort_docs(folder_to_sort)

    # Check if the files were moved to the correct folders
    logs_folder = folder_to_sort / "logs"
    mail_folder = folder_to_sort / "mail"

    assert (logs_folder / "file1.txt").exists()
    assert (logs_folder / "file3.txt").exists()
    assert (logs_folder / "file4.txt").exists()
    assert not (folder_to_sort / "file2.mail").exists()

    assert (mail_folder / "file2.mail").exists()

    # Clean up the temporary files
    (logs_folder / "file1.txt").unlink()
    (logs_folder / "file3.txt").unlink()
    (logs_folder / "file4.txt").unlink()
    (mail_folder / "file2.mail").unlink()
    logs_folder.rmdir()
    mail_folder.rmdir()
    folder_to_sort.rmdir()



## Testing for count_file_types

def test_count_file_types(monkeypatch, tmp_path):
    # Create a temporary directory with files
    test_directory = tmp_path / "test_directory"
    test_directory.mkdir()
    (test_directory / "file1.txt").write_text("This is a text file.")
    (test_directory / "file2.txt").write_text("This is another text file.")
    (test_directory / "file3.jpg").write_text("This is an image file.")
    (test_directory / "file4.jpg").write_text("This is another image file.")
    (test_directory / "file5.txt").mkdir()

    # Execute the count_file_types function
    monkeypatch.setattr("builtins.input", lambda _: str(test_directory))
    file_types = count_file_types(None, None)

    # Check if the file types and counts are correct
    assert file_types == {".txt": 2, ".jpg": 2}

    # Clean up the temporary files and directory
    (test_directory / "file1.txt").unlink()
    (test_directory / "file2.txt").unlink()
    (test_directory / "file3.jpg").unlink()
    (test_directory / "file4.jpg").unlink()
    (test_directory / "file5.txt").rmdir()
    test_directory.rmdir()


## Testing for menu_tasks

def test_menu_tasks(monkeypatch, capsys):
    # Mock user input for the menu prompt
    monkeypatch.setattr("builtins.input", lambda _: "1")

    # Execute the menu_tasks function
    menu_tasks()

    # Check if the expected output is captured
    captured = capsys.readouterr()
    assert "Select one of these Automation Tasks:" in captured.out
    assert "Enter your choice (1-5): " in captured.out

    # Clean up the captured output
    sys.stdout = sys.__stdout__



# Run the test
if __name__ == "__main__":
    pytest.main()

