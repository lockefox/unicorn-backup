"""
Main() CLI

.. moduleauthor: John Purcell <jpurcell.ee@gmail.com>
"""

from . import __version__, __pkg_name__

import click
from loguru import logger
from click_loguru import ClickLoguru

click_loguru = ClickLoguru(
    __pkg_name__,
    __version__,
    retention=0,
    log_dir_parent="/tmp/unicorn-backup"
)

@click_loguru.logging_options
@click.group()
@click_loguru.stash_subcommand()
@click.version_option(__version__, prog_name=__pkg_name__)
def cli(verbose, quiet, logfile, profile_mem):
    """cli main() wrapper"""
    pass

