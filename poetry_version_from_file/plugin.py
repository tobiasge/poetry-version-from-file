import os

from cleo.io.io import IO
from poetry.plugins.plugin import Plugin
from poetry.poetry import Poetry

DEFAULT_VERSION_FILE = "VERSION"
INVALID_VERSION_MARKER = "invalid"
PYPROJECT_TABLE = "tool.poetry.plugin.version-from-file"
VERSION_FILE_KEY = "file"


class PoetryVersionFromFile(Plugin):
    def activate(self, poetry: Poetry, io: IO):
        # Try to get settings
        plugin_settings = (
            poetry.pyproject.data.get("tool", {})
            .get("poetry", {})
            .get("plugins", {})
            .get("version-from-file", {})
        )
        current_version_file = plugin_settings.get(VERSION_FILE_KEY, DEFAULT_VERSION_FILE)

        if not os.path.isfile(current_version_file):
            io.write_error_line(f"Version file ({current_version_file}) is missing")
            poetry.package.version = INVALID_VERSION_MARKER
            return
        with open(current_version_file, "r", encoding="UTF-8") as version_file:
            version_str = version_file.read().strip()
            poetry.package.version = version_str
