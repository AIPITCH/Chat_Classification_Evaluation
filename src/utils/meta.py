"""
Utility module to manage meta info.
"""

import platform

from rich.console import Console

from . import __curr_year__, __license__

APP_VERSION = "dev"
DEVICE_MODEL = f"{platform.python_implementation()} {platform.python_version()}"
SYSTEM_VERSION = f"{platform.system()} {platform.release()}"
LANG_CODE = "en"


def print_meta():
    """
    Prints meta-data of the script.
    """
    console = Console()
    console.log("[bold]Channel Classifier[/bold]")
    console.log(f"Licensed under the terms of the {__license__}")
    console.log(f"AIL project by CIRCL - 2026-{__curr_year__} - https://www.ail-project.org")
    console.log(f"Device: {DEVICE_MODEL} - Channel Classifier: {APP_VERSION}")
    console.log(f"System: {SYSTEM_VERSION} ({LANG_CODE.upper()})", end="\n\n")
