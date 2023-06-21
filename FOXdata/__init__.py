"""A repository with MD data used by the `Auto-FOX <https://github.com/nlesc-nano/auto-FOX>`_ tests."""  # noqa: E501

from pathlib import Path
from ._version import __version__ as __version__

_ROOT = Path(__file__).parent
ARMC_DIR = _ROOT / "armc"
ARMCPT_DIR = _ROOT / "armcpt"

__all__ = ["ARMC_DIR", "ARMCPT_DIR", "__version__"]
del Path, _ROOT
