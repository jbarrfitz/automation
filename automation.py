from rich.console import Console
from rich.prompt import Prompt
from commands.count_file_types import count_file_types
from commands.create_directory import create_directory_if_not_exists
from commands.handle_deleted_user import delete_user
from commands.sort_docs import sort_docs
from commands.parse_log import parse_log
import os


def main():
    """
    Main menu and entry point for the automation app.
    :return: None
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    console.print("[gold1]Welcome to the[/gold1] [purple]JBF Automation App![/purple]")
    while True:
        console.print("\n[turquoise2]Please make a numeric selection. Default is 6.[/turquoise2]")
        console.print("\n1. Create Directory\n2. Delete User\n3. Sort Documents\n4. Parse Log File\n5. Count File "
                      "Types\n6. Exit")
        menu_selection = Prompt.ask("[turquoise2]Please enter your selection[/turquoise2]")
        if menu_selection == "1":
            dir_name = Prompt.ask("[yellow]Please enter the new directory name. It will be stored in [/yellow] ["
                                  "turquoise2]./assets[/turquoise2]")
            new_directory_path = os.path.join("./assets/", dir_name)
            console.print(create_directory_if_not_exists(new_directory_path))
        elif menu_selection == "2":
            user_name = Prompt.ask("[yellow]Please enter the username that has been deleted.[/yellow]")
            console.print(delete_user(user_name))
        elif menu_selection == "3":
            sort_path = Prompt.ask("[yellow]Please enter the path of the directory you wish to sort.[/yellow]")
            console.print(sort_docs(sort_path))
        elif menu_selection == "4":
            log_path = Prompt.ask("[yellow]Please enter the path of the log you wish to parse[/yellow]")
            console.print(parse_log(log_path))
        elif menu_selection == "5":
            count_path = Prompt.ask("[yellow]Please enter the path where you would like to count the number of file "
                                    "types[/yellow]")
            console.print(count_file_types(count_path))
        else:
            break


if __name__ == "__main__":
    console = Console()
    main()
