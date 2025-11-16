from pathlib import Path
from rich import print

def show_path():
    """
        Shows path of input directory.
    """
    current_dir = Path.cwd()
    print(f"Current dir: [green]{current_dir}[/green]")