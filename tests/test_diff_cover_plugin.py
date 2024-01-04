import json
import os
from unittest.mock import patch

from diff_cover.diff_quality_tool import main

from pyright_diff_quality_plugin.pyright_plugin import PyrightViolationReporter


def test_plugin_can_load():
    main(["diff-quality", "--violations", "pyright"])

@patch("pyright_diff_quality_plugin.pyright_plugin.exists")
def test_given_file_does_not_exist_then_return_no_violations(mock_exists):
    mock_exists.return_value = False

    reporter = PyrightViolationReporter()
    violations = reporter.violations("")
    assert violations == []

@patch("pyright_diff_quality_plugin.pyright_plugin.exists")
@patch("pyright_diff_quality_plugin.pyright_plugin.subprocess.run")
def test_given_file_does_exist_and_test_json_used_then_return_expected_violations(mock_subprocess, mock_exists):
    with open(os.path.join("tests", "test_data","test_json.json")) as f:
        mock_subprocess.return_value.stdout = f.read()
    mock_exists.return_value = True

    reporter = PyrightViolationReporter()
    violations = reporter.violations("")
    assert len(violations) == 260
