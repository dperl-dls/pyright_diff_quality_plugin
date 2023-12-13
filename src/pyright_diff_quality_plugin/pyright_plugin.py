import json
import subprocess

from diff_cover.command_runner import run_command_for_code
from diff_cover.hook import hookimpl as diff_cover_hookimpl
from diff_cover.violationsreporters.base import BaseViolationReporter, Violation


def run_process_parse_json(command):
    result = subprocess.run(command, capture_output=True, text=True)
    output = json.loads(result.stdout)
    return output

def get_violations(output):
    violations: list[Violation] = []
    if output["summary"]["errorCount"] == 0:
        return violations
    diagnostics = output["generalDiagnostics"]
    for diagnostic in diagnostics:
        if diagnostic["severity"] == "error":
            violations.append(Violation(diagnostic["range"]["start"]["line"], diagnostic["message"]))
    return violations

class PyrightViolationReporter(BaseViolationReporter):
    supported_extensions = ['py']
    def __init__(self):
        super(PyrightViolationReporter, self).__init__('pyright')

    def violations(self, src_path):
        pyright_output = run_process_parse_json(["pyright","--outputjson",src_path])
        return get_violations(pyright_output)

    def measured_lines(self, src_path):
        return None

    @staticmethod
    def installed():
        return run_command_for_code(["pyright","--verison"]) == 0

@diff_cover_hookimpl
def diff_cover_report_quality(*args, **kwargs):
    return PyrightViolationReporter()
