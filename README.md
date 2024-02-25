## Poetry version from file plugin

This is a simple Poetry plugin that loads the project version dynamically from a `VERSION` file.

### Usage
Add the plugin to the build system requirements:
```toml
[build-system]
requires = ["poetry-core", "poetry-version-from-file"]
```

The create a file named `VERSION` and put your projects version nummber in it.

If you already have a file containing your projects version you can configure the plugin to use that file with the following settings in your `pyproject.toml`:

```toml
[tool.poetry.plugins.version-from-file]
file = "VERSION.txt"
```
