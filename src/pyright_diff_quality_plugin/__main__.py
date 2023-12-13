from argparse import ArgumentParser

from . import __version__

__all__ = ["main"]


def main(args=None):
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args(args)

    print("This project is meant to be used as a plugin for diff_cover: https://github.com/Bachmann1234/diff_cover diff-quality tool")


# test with: python -m pyright_diff_quality_plugin
if __name__ == "__main__":
    main()
