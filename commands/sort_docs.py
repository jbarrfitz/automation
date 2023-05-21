import os
import shutil


def sort_docs(path):
    if not os.path.exists(path):
        return f"[red]The path you entered: [/red][turquoise2]{path}[/turquoise2] [red]does not exist.[/red]"

    for item in os.listdir(path):
        pass