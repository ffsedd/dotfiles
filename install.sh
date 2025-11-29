#!/usr/bin/env bash

# dotfiles directory = script directory
dotfiledir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ ! -d "${dotfiledir}" ]]; then
    echo "Directory ${dotfiledir} does not exist. Aborting."
    exit 1
fi

echo "Changing to ${dotfiledir}"
cd "${dotfiledir}" || exit

python3 ${dotfiledir}/make_symlinks.py

echo "Installation Complete!"

