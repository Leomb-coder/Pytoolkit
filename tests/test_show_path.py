from typer.testing import CliRunner
from pytoolkit.cli import app

runner = CliRunner()

def test_show_path(tmp_path):
    # Create a temporary folder to test the show-path command
    folder = tmp_path / "test_folder"
    folder.mkdir()

    with runner.isolated_filesystem(temp_dir=folder):
        result = runner.invoke(app, ["show-path"])
        
        assert result.exit_code == 0
        assert '/' in result.stdout or '\\' in result.stdout
        assert str(folder) in result.stdout
        
        # When prompted with pytest -s:
        # This test should output Current dir: /tmp/pytest-of-leomb/pytest-4/test_show_path0/test_folder/*temporary_dir*
        print(result.stdout)