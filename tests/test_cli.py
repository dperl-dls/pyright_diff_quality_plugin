import subprocess
import sys

from pyright_diff_quality_plugin import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "pyright_diff_quality_plugin", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
