import os
import sys
import shutil
import subprocess
from pathlib import Path

DIST = Path('build')


def test_isdir() -> None:
    lib = None
    try:
        out = subprocess.run(f'python setup.py build', shell=True, check=True)
        out.check_returncode()

        lib = DIST / 'lib'
        sys.path.insert(1, str(lib))

        from FOXdata import ARMC_DIR, ARMCPT_DIR
        for root in (ARMC_DIR, ARMCPT_DIR):
            assert os.path.isfile(root / 'armc.hdf5')

            for _folder in os.listdir(root):
                folder = root / _folder
                if not os.path.isdir(folder):
                    continue

                for file in os.listdir(folder):
                    _, ext = os.path.splitext(file)
                    assert ext in {'.xyz', '.dill'}
    finally:
        if lib in sys.path:
            i = sys.path.index(lib)
            del sys.path[i]
        if os.path.isdir(DIST):
            pass  # shutil.rmtree(DIST)
