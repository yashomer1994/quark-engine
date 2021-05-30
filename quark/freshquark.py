# -*- coding: utf-8 -*-
# This file is part of Quark-Engine - https://github.com/quark-engine/quark-engine
# See the file 'LICENSE' for copying permission.
"""
Freshquark is a command-line interface to download the latest Quark rules
"""

import os
import subprocess

from quark import config
from quark.utils.colors import green
from quark.utils.out import print_warning, print_info, print_success


def download():
    """
    Download the latest quark-rules from https://github.com/quark-engine/quark-rules.

    :return: None
    """

    if not os.path.isdir(config.DIR_PATH):

        try:
            result = subprocess.run(
                [
                    "git",
                    "clone",
                    "https://github.com/quark-engine/quark-rules",
                    config.DIR_PATH,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            if result.returncode == 0:
                # Download successful
                print_success("Complete downloading the latest quark-rules")

        except FileNotFoundError:

            print_warning("FileNotFoundError with git clone")

        except subprocess.CalledProcessError as error:

            network_unavailable = "unable to access"

            if network_unavailable in error.stderr.decode("utf-8"):
                print_warning(
                    f"Your network is currently unavailable, "
                    f"you can use {green('freshquark')} "
                    "to update the quark-rules later!\n"
                )
    else:
        try:
            result = subprocess.run(
                [
                    "git",
                    "-C",
                    config.DIR_PATH,
                    "pull",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )

            if result.returncode == 0:
                # Download successful
                print_success("Complete downloading the latest quark-rules")

        except subprocess.CalledProcessError as error:

            network_unavailable = "unable to access"

            if network_unavailable in error.stderr.decode("utf-8"):
                print_warning(
                    f"Your network is currently unavailable, "
                    f"you can use {green('freshquark')} "
                    "to update the quark-rules later!\n"
                )


def entry_point():
    """
    The command-line entry point for freshquark. It will download the latest quark-rules.

    :return: None
    """
    print_info(f"Download the latest rules from {config.SOURCE}")
    download()


if __name__ == "__main__":
    pass
