import os
from pathlib import Path

import pytest
from FOXdata import ARMC_DIR, ARMCPT_DIR


@pytest.mark.parametrize('root', [ARMC_DIR, ARMCPT_DIR])
def test_isdir(root: Path) -> None:
    assert os.path.isfile(root / 'armc.hdf5')

    for _folder in os.listdir(root):
        folder = root / _folder
        if not os.path.isdir(folder):
            continue

        for file in os.listdir(folder):
            _, ext = os.path.splitext(file)
            assert ext in {'.xyz', '.dill'}
