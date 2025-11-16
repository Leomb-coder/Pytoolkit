from pathlib import Path
from rich import print

def show_parent():
    """
        Shows parent of input directory.
    """
    parent_dir = Path.cwd().parent
    print(f"Parent dir: [green]{parent_dir}[/green]")