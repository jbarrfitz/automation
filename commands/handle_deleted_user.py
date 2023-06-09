import shutil
import os


def delete_user(user):
    user_folder = os.path.join('assets/user-docs/', user)
    dest_folder = 'assets/user-docs/temp_' + user
    if not os.path.exists(user_folder):
        return f"[red]User[/red] [turquoise2 bold]{user}[/turquoise2 bold] [red]does not exist. Deletion not " \
               f"processed.[/red]"
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    for item in os.listdir(user_folder):
        user_item = os.path.join(user_folder, item)
        destination_item = os.path.join(dest_folder, item)
        shutil.move(user_item, destination_item)
    return f"[green]User[/green] [turquoise2 bold]{user}[/turquoise2 bold] [green]successfully deleted.[/green]"
