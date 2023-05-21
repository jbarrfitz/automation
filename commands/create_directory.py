import os


def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        return f"[green]Directory[/green] [turquoise2]'{directory_path}'[/turquoise2] created."
    else:
        return f"[red]Directory[/red] [turquoise2]'{directory_path}'[/turquoise2] [red]already exists.[/red]"
