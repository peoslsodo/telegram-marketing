
import subprocess
import sys
from typing import Optional

from . import __version__ as telegram_ver
from .constants import BOT_API_VERSION


def _git_revision() -> Optional[str]:
    try:
        output = subprocess.check_output(
            ["git", "describe", "--long", "--tags"], stderr=subprocess.STDOUT
        )
    except (subprocess.SubprocessError, OSError):
        return None
    return output.decode().strip()


def print_ver_info() -> None:
    """Prints version information for python-telegram-bot, the Bot API and Python."""
    git_revision = _git_revision()
    print(f"python-telegram-bot {telegram_ver}" + (f" ({git_revision})" if git_revision else ""))
    print(f"Bot API {BOT_API_VERSION}")
    sys_version = sys.version.replace("\n", " ")
    print(f"Python {sys_version}")


def main() -> None:
    """Prints version information for python-telegram-bot, the Bot API and Python."""
    print_ver_info()


if __name__ == "__main__":
    main()