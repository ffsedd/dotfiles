#!/usr/bin/env python3
import logging
import sys
from pathlib import Path

# ============================
# Setup logging
# ============================
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ============================
# Dotfiles paths
# ============================
dotfiledir = Path(__file__).resolve().parent
homedir = dotfiledir / "home"
home = Path.home()

if not homedir.exists():
    logger.error(f"Directory {homedir} does not exist. Aborting.")
    sys.exit(1)


# ============================
# Functions
# ============================
def symlink(src: Path, dest: Path) -> None:
    if dest.exists() or dest.is_symlink():
        dest.unlink()
        logger.debug(f"Removed existing file/symlink: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.symlink_to(src)
    logger.info(f"Created symlink: {dest} → {src}")


def install_dir(src_dir: Path, dest_dir: Path) -> None:
    for item in src_dir.iterdir():
        dest_item = dest_dir / item.name
        if item.is_dir():
            install_dir(item, dest_item)  # recursive
        else:
            symlink(item, dest_item)


# ============================
# Run installation
# ============================
install_dir(homedir, home)
logger.info(f"{__file__} Installation Complete!")
