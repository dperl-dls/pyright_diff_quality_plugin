from importlib.metadata import version

__version__ = version("pyright_diff_quality_plugin")
del version

__all__ = ["__version__"]
