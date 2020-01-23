import click
import sys
from pep582 import patch


@click.group()
def main():
    pass


@click.command()
@click.option('--bin', default=False, help='create __pypackages__/bin and add to PATH')
def install(bin):
    patch.update_site_py(True, bin)
    patch.update_bash_rc(True, bin)


@click.command()
@click.option('--bin', default=False, help='create __pypackages__/bin and add to PATH')
def uninstall(bin):
    patch.update_site_py(False, bin)
    patch.update_bash_rc(False, bin)


@click.command()
def freeze():
    sys.path = [sys.path[0]]
    print(sys.path)
    from pip.__main__ import _main
    _main()


if __name__ == '__main__':
    main()
