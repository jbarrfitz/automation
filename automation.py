from rich.console import Console
from rich.prompt import Prompt
from commands.create_directory import create_directory_if_not_exists
from commands.handle_deleted_user import delete_user
from commands.sort_docs import sort_docs
import os


def main():
    """
    Main menu and entry point for the automation app.
    :return: None
    """
    console.print("[gold1]Welcome to the[/gold1] [purple]JBF Automation App![/purple]")
    console.print("[turquoise2]Please make a numeric selection. Default is 5.[/turquoise2]")
    console.print("\n1. Create Directory\n2. Delete User\n3. Sort Documents\n4. Parse Log File\n5. Exit")
    menu_selection = Prompt.ask(" > ")
    if menu_selection == "1":
        console.print("Please enter the new directory name. It will be stored in [turquoise2]./assets[/turquoise2]")
        dir_name = Prompt.ask(" > ")
        new_directory_path = os.path.join("./assets/", dir_name)
        response = create_directory_if_not_exists(new_directory_path)
        console.print(response)
    if menu_selection == "2":
        console.print("Please enter the username that has been deleted.")
        user_name = Prompt.ask(" > ")
        delete_response = delete_user(user_name)
        console.print(delete_response)
    if menu_selection == "3":
        console.print("Please enter the path you wish to sort")
        sort_path = Prompt.ask(" > ")
        sort_response = sort_docs(sort_path)
if __name__ == "__main__":
    console = Console()
    main()
