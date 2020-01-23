import os, sys


def load_pypackagesa():
    path = os.path.join(os.path.abspath(sys.modules['__main__'].__file__), '__pypackages__')

    if os.path.exists(path):
        lib = os.path.join(path, '{}.{}/lib'.format(sys.version_info.major, sys.version_info.minor))
        if not os.path.exists(lib):
            os.makedirs(lib)
            os.makedirs('{}/bin'.format(lib))
            bin = os.path.abspath(os.path.join(path, 'bin'))
            if os.path.islink(bin):
                os.unlink(os.path.abspath(os.path.join(path, 'bin')))
            os.symlink(os.path.abspath(os.path.join(lib, 'bin')), os.path.abspath(os.path.join(path, 'bin')))
        sys.path.insert(0, lib)
        if 'pip' in sys.argv or sys.argv[0].endswith('pip'):
            if 'install' in sys.argv and ('-t' not in sys.argv and '--target' not in sys.argv):
                sys.argv.extend(['-t', lib])
