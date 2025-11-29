#!/usr/bin/env python3
import sys
from pathlib import Path

from logger import setup_logger

logger = setup_logger(Path(__file__).stem)

dotfiledir = Path(__file__).resolve().parent
homedir = dotfiledir / "home"
home = Path.home()

if not homedir.exists():
    logger.error(f"Directory {homedir} does not exist. Aborting.")
    sys.exit(1)


def symlink(src: Path, dest: Path) -> None:
    """Create a symlink from src to dest, removing existing files."""
    if dest.exists() or dest.is_symlink():
        dest.unlink()
        logger.debug(f"Removed existing file/symlink: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.symlink_to(src.resolve())
    logger.info(f"Created symlink: {dest} → {src}")


def install_dir(src_dir: Path, dest_dir: Path) -> None:
    """Recursively install files from src_dir into dest_dir."""
    for item in src_dir.iterdir():
        dest_item = dest_dir / item.name
        if item.is_dir():
            # Option 1: symlink the entire directory
            # symlink(item, dest_item)
            # Option 2: recurse into directory
            dest_item.mkdir(exist_ok=True)
            install_dir(item, dest_item)
        else:
            symlink(item, dest_item)


install_dir(homedir, home)
logger.info(f"{__file__} Installation Complete!")
