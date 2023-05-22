import os
import shutil


def sort_docs(path):
    if not os.path.exists(path):
        return f"[red]The path you entered: [/red][turquoise2]{path}[/turquoise2] [red]does not exist.[/red]"
    for item in os.listdir(path):
        root, ext = os.path.splitext(item)
        ext = ext.lstrip(".")
        if not os.path.exists(os.path.join(path, ext)):
            os.makedirs(os.path.join(path, ext))
        shutil.move(os.path.join(path, item), os.path.join(path, ext))
    return f"[green]All files in {path} have been successfully sorted.[/green]"
