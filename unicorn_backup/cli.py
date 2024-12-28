"""
Main() CLI

.. moduleauthor: John Purcell <jpurcell.ee@gmail.com>
"""

from . import __version__, __pkg_name__
from . import tools

import pathlib

import click
from loguru import logger
from click_loguru import ClickLoguru

click_loguru = ClickLoguru(
    __pkg_name__, __version__, retention=0, log_dir_parent="/tmp/unicorn-backup"
)


@click_loguru.logging_options
@click.group()
@click_loguru.stash_subcommand()
@click.version_option(__version__, prog_name=__pkg_name__)
def cli(verbose, quiet, logfile, profile_mem):
    """cli main() wrapper"""
    pass


@click.command()
@click_loguru.init_logger()
@click.option(
    "--application-key-id",
    envvar="B2_APPLICATION_KEY_ID",
    help="b2 application_key_id",
    type=str,
)
@click.option(
    "--application-key",
    envvar="B2_APPLICATION_KEY",
    help="b2 application_key",
    type=str,
)
@click.option(
    "--bucket-name",
    envvar="B2_BUCKET_NAME",
    help="Name of b2 bucket",
    type=str,
)
@click.option(
    "--path-header",
    help="b2 path to sync to: b2://bucket-name/path-header",
    type=str,
)
@click.argument(
    "src_dir",
)
@click.option("--ignore-year", is_flag=True, help="ignore YYYY-MM-DD folder naming")
@click.option(
    "--force-upload", is_flag=True, help="skip checking duplicates and force sync all"
)
@click.option(
    "--dry-run", is_flag=True, help="Skip `b2 sync` step and just run read-only logic"
)
def sync(
    src_dir: click.Path,
    application_key_id,
    application_key,
    bucket_name,
    path_header,
    ignore_year,
    force_upload,
    dry_run,
):
    """sync all folders in `src_dir` to `b2://bucket_name/path_header`"""
    logger.info("Gathering `src_dir` folder list")
    src_folders = tools.list_dirs(pathlib.Path(src_dir))

    for x in src_folders:
        logger.info(f"-- {x.name}")


@click.command()
@click_loguru.init_logger()
@click.option(
    "--application-key-id",
    envvar="B2_APPLICATION_KEY_ID",
    help="b2 application_key_id",
    type=str,
)
@click.option(
    "--application-key",
    envvar="B2_APPLICATION_KEY",
    help="b2 application_key",
    type=str,
)
@click.option(
    "--bucket-name",
    envvar="B2_BUCKET_NAME",
    help="Name of b2 bucket",
    type=str,
)
@click.option(
    "--path-header",
    help="b2 path to sync to: b2://bucket-name/path-header",
    type=str,
)
@click.argument(
    "src_dir",
)
@click.option(
    "--force-upload", is_flag=True, help="skip checking duplicates and force sync all"
)
@click.option(
    "--dry-run", is_flag=True, help="Skip `b2 sync` step and just run read-only logic"
)
def sync_single(
    src_dir: click.Path,
    application_key_id,
    application_key,
    bucket_name,
    path_header,
    force_upload,
    dry_run,
):
    """utility for uploading a single folder to b2 path"""
    pass


cli.add_command(sync)
cli.add_command(sync_single)

if __name__ == "__main__":
    cli()
