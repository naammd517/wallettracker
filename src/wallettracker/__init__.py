"""WalletTracker: Monitors a set of wallet addresses and logs balance changes over time."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]