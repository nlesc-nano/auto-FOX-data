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

        lib = str(DIST / 'lib')
        sys.path.insert(1, lib)

        from FOXdata import ARMC_DIR, ARMCPT_DIR
        expected_length = {
            ARMC_DIR: 101,
            ARMCPT_DIR: 303,
        }

        for root in (ARMC_DIR, ARMCPT_DIR):
            folder_list = [root / f for f in os.listdir(root) if os.path.isdir(root /f)]
            assert os.path.isfile(root / 'armc.hdf5')
            assert len(folder_list) == expected_length[root]

            for folder in folder_list:
                for file in os.listdir(folder):
                    _, ext = os.path.splitext(file)
                    assert ext in {'.xyz', '.dill'}

    finally:
        if lib in sys.path:
            i = sys.path.index(lib)  # type: ignore[arg-type]
            del sys.path[i]
        if os.path.isdir(DIST):
            shutil.rmtree(DIST)
