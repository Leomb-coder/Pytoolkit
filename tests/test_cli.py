from typer.testing import CliRunner
from pytoolkit.cli import app

runner = CliRunner()

print(app)  # Debug: Print the app object to verify it's correctly imported