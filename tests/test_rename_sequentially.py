from typer.testing import CliRunner
from pytoolkit.cli import app
from rich import print
from pathlib import Path

runner = CliRunner()

def test_rename_sqt(tmp_path):

    with runner.isolated_filesystem(temp_dir=tmp_path):
        inner = Path.cwd()
        # Create 10 files inside temporary folder
        for n in range(10):
            (inner / f"fi{n}le.txt").touch()
        
        # [function] [DIRECTORY] [new_file_name] [--dry]
        
        # This will display the result using --dry input
        result_dry = runner.invoke(app, ["rename-sqt", ".", "fileleo", "--dry"])
        
        # This will display the result without --dry input
        result_no_dry = runner.invoke(app, ["rename-sqt", ".", "fileleo"])
        
        assert result_dry.exit_code == 0
        assert 'fileleo' in result_dry.stdout
        assert '[DRY]' in result_dry.stdout
        
        assert result_no_dry.exit_code == 0
        assert 'fileleo' in result_no_dry.stdout
        assert '[DRY]' not in result_no_dry.stdout
        # This test should print files renamed from (1) to (10)
        print(result_dry.stdout)
        print(result_no_dry.stdout)