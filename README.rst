pyright_diff_quality_plugin
===========================

|code_ci| |coverage| |pypi_version| |license|

A plugin for `diff_cover <https://github.com/Bachmann1234/diff_cover>`_ to enable Pyright as a quiality-checking tool.

============== ==============================================================
Source code    https://github.com/dperl-dls/pyright_diff_quality_plugin
Releases       https://github.com/dperl-dls/pyright_diff_quality_plugin/releases
============== ==============================================================

For example, with diff-cover installed, you can run::

    $ diff-quality --violations=pyright --fail-under=100

To get a task which will fail if any modified code doesn't meet Pyright standards.

.. |code_ci| image:: https://github.com/dperl-dls/pyright_diff_quality_plugin/actions/workflows/code.yml/badge.svg?branch=main
    :target: https://github.com/dperl-dls/pyright_diff_quality_plugin/actions/workflows/code.yml
    :alt: Code CI

.. |coverage| image:: https://codecov.io/gh/dperl-dls/pyright_diff_quality_plugin/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/dperl-dls/pyright_diff_quality_plugin
    :alt: Test Coverage

.. |pypi_version| image:: https://img.shields.io/pypi/v/pyright_diff_quality_plugin.svg
    :target: https://pypi.org/project/pyright_diff_quality_plugin
    :alt: Latest PyPI version

.. |license| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0
    :alt: Apache License

..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

