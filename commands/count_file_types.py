import os


def count_file_types(path):
    if not os.path.exists(path):
        return f"[red]The path you provided, [/red][turquoise2]{path}[/turquoise2][red], does not exist.[/red]"
    file_types = set()
    for item in os.listdir(path):
        root, ext = os.path.splitext(item)
        ext = ext.lstrip(".")
        file_types.add(ext)
    return f"[green]There are [/green][turquoise2]{len(file_types)}[/turquoise2] [green]file types in [/green][" \
           f"turquoise2]{path}[/turquoise2]"
