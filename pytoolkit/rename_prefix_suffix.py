from pathlib import Path
from rich import print

def rename_ps(directory, prefix="", suffix="", dry=False):

    """
    Rename all files in a directory using prefixes and suffixes in this pattern:

        {prefix}{current_file_name}{suffix}

    Both {prefix} and {sufix} use is optinal.
    
    Example output:
        new_photo_leomb.jpg
        new_music_leomb.mp3
        new_video_leomb.mp4

    Arguments:
        directory   -- Path to the folder containing files to rename
        prefix      -- Prefix used before the file name
        sufix       -- Sufix used after the file name
    """

    directory = Path(directory)
    if not directory.exists():
        print(f"[red]Directory does not exist![/red]")
        return
    for file in directory.iterdir():
        new_name = f"{prefix}{file.stem}{suffix}{file.suffix}"
        new_path = file.with_name(new_name)
        if dry:
            print(f"[green][DRY][/green] {file.name} [red]-->[/red] {new_name}")
        else:
            file.rename(new_path)
            print(f"[green]Renamed: [/green]{file.name} [red]-->[/red] {new_name}")