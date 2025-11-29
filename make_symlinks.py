#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# script directory = dotfiles base
dotfiledir = Path(__file__).resolve().parent
homedir = dotfiledir / "home"
home = Path.home()

if not homedir.exists():
    print(f"Directory {homedir} does not exist. Aborting.")
    sys.exit(1)

def symlink(src: Path, dest: Path):
    if dest.exists() or dest.is_symlink():
        dest.unlink()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.symlink_to(src)
    print(f"Created symlink: {dest} → {src}")

def install_dir(src_dir: Path, dest_dir: Path):
    for item in src_dir.iterdir():
        dest_item = dest_dir / item.name
        if item.is_dir():
            install_dir(item, dest_item)  # recursive
        else:
            symlink(item, dest_item)

install_dir(homedir, home)
print(f"{__file__} Installation Complete!")

