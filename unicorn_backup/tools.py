"""utilities for unicorn_backup"""
from typing import List
import pathlib


def list_dirs(src_path: pathlib.Path) -> List[pathlib.Path]:
    """lists all dirs in a given path (not subdirs)

    NOTE: C&P from google AI

    Args:
        src_path (:obj:`pathlib.Path`): path to scan

    Returns:
        list: returns list of `pathlib.Path`

    """
    for x in src_path.iterdir():
        if x.is_dir():
            yield x
