"""

Tests for unicorn_backup.tools

..moduleauthor:: John Purcell <jpurcell.ee@gmail.com>
"""

import os
import pathlib

from unicorn_backup import tools

def test_list_dirs(tmp_path):
    files = ["test.txt", "not_dir"]
    folders = ["a", "b", "yes_dir"]

    for folder in folders:
        os.makedirs(f"{tmp_path}/{folder}")

    for file in files:
        pathlib.Path.touch(tmp_path / file)

    dirs = tools.list_dirs(tmp_path)

    assert len([x for x in dirs]) == 3
