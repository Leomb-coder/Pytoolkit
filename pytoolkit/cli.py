import typer
from . import rename_prefix_suffix, rename_sequentially, show_path, show_parent

app = typer.Typer(name='Command Line Leomb')

app.command()(show_path.show_path)

app.command()(show_parent.show_parent)

app.command()(rename_prefix_suffix.rename_ps)

app.command()(rename_sequentially.rename_sqt)

if __name__ == "__main__":
    app()