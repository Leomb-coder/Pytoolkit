from pathlib import Path
from rich import print
import typer

def rename_sqt(
    directory: Path,
    new_file_name: str = typer.Option("", "--nfn", "-n"),
    dry: bool = typer.Option(False, "--dry", "-d")
    ):
    
    """
    Rename all files in a directory sequentially using the pattern:

        {new_file_name}_(<number>){extension}

    Example output:
        photo_(1).jpg
        photo_(2).jpg
        photo_(3).jpg

    Arguments:
        directory      -- Path to the folder containing files to rename
        new_file_name  -- Base name used before the sequence number
        dry            -- If True, only show actions without renaming files
    """

    i = 0
    directory = Path(directory)
    for file in directory.iterdir():
        i += 1
        new_name = f"{new_file_name}_({i}){file.suffix}"
        new_path = file.with_name(new_name)
        if dry:
            print(f'[green][DRY] [/green]{file.name} --> {new_name}')
        else:
            file.rename(new_path)
            print(f"[green]Renamed: [/green]{file.name} --> {new_name}")