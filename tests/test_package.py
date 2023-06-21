from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any, NamedTuple

import h5py
import yaml
import pytest
import numpy as np
from nanoutils import RecursiveKeysView, RecursiveItemsView
from assertionlib import assertion

from FOXdata import ARMC_DIR, ARMCPT_DIR


class DSetTuple(NamedTuple):
    shape: tuple[int, ...]
    dtype: np.dtype[Any]


def load_h5py_data() -> dict[str, dict[str, DSetTuple]]:
    with open(Path("tests") / "h5py_data.yaml", "r", encoding="utf8") as f:
        dct = yaml.load(f, Loader=yaml.SafeLoader)
    for sub_dict in dct.values():
        for k, v in sub_dict.items():
            sub_dict[k] = DSetTuple(tuple(v["shape"]), np.dtype(v["dtype"]))
    return dct


H5PY_DICT = load_h5py_data()
PARAMS = dict(
    armc=("armc", ARMC_DIR, 101),
    armcpt=("armcpt", ARMCPT_DIR, 303),
)


@pytest.mark.parametrize("name,path,length", PARAMS.values(), ids=PARAMS)
class TestPackage:
    def test_hdf5(self, name: str, path: Path, length: int) -> None:
        ref = H5PY_DICT[name]
        with h5py.File(path / "armc.hdf5", "r") as f:
            assertion.eq(ref.keys(), RecursiveKeysView(f))  # type: ignore[abstract]
            for name, dset in RecursiveItemsView(f):  # type: ignore[abstract]
                assertion.eq(dset.shape, ref[name].shape, message=f"{name} shape")
                assertion.eq(dset.dtype, ref[name].dtype, message=f"{name} dtype")

    def test_files(self, name: str, path: Path, length: int) -> None:
        pattern = re.compile(r"md(\.([0-9]+))?")
        root_dirs = [i for i in os.listdir(path) if pattern.fullmatch(i)]
        assertion.len_eq(root_dirs, length)
        for f in root_dirs:
            for file in os.listdir(path / f):
                _, ext = os.path.splitext(file)
                assertion.contains({'.xyz', '.dill'}, ext, message=file)
