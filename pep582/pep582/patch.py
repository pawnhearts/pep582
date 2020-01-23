import site, os, sys, argparse

CODE = """""try:
    from pep582.site import load_pypackages, load_bin
    load_pypackages({})
except ImportError:
    pass # uninstalled maybe
"""

def update_site_py():
    parser = argparse.ArgumentParser()
    parser.add_argument('--uninstall', action='store_false',
                        default=True,
                        dest='install',
                        help='uninstall. remove itself from site.py')

    parser.add_argument('--bin', action='store_bin',
                        default=False,
                        dest='bin',
                        help='add __pypackages__/bin to PATH')

    args = parser.parse_args()

    try:
        if args.install:
            if not hasattr(site, 'pep582'):
                with open(site.__file__, 'a') as f:
                    f.write(CODE.format(args.bin))
                print('{} succesfully patched'.format(site.__file__))
                print('try creating __pypackages__ in some directory')
                print('pip install inside that directory would install into __pypackages__ by default')
                print('good luck!')
            else:
                print('{} already patched'.format(site.__file__))
        else:
            if hasattr(site, 'pep582'):
                with open(site.__file__, 'r') as f:
                    site_content = f.read()
                with open(site.__file__+'_', 'w') as f:
                    f.write(site_content.replace(CODE.format(False, '').replace(CODE.format(True, '')))
                os.rename(site.__file__+'_', site.__file__)
                print('{} succesfully patched'.format(site.__file__))
                print('pep582 removed')
            else:
                print('pep582 not found in {} '.format(site.__file__))

    except PermissionError:
        os.execvp(sys.executable, ['sudo'] + sys.argv)


