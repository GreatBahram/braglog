# Contributing
To contribute to this tool, first checkout the code. Then create a new virtual environment:
```shell
cd braglog
python -m venv .venv
source .venv/bin/activate
```
Now install the dependencies and test dependencies:
```shell
pip install -e '.[dev]'
```
Or if you are using [uv](https://docs.astral.sh/uv/):
```shell
uv sync --extra dev
```
To run the tests:
```
uv run pytest .
```
To help ensure consistent code quality that follows our guidelines, [pre-commit](https://pre-commit.com/install) may be used. We have git hooks defined which will execute before commit. To install the hooks:

```shell
pre-commit install
```
## Release process
To release a new version:
1. Update docs/changelog.md with the new changes.
2. Update the version number in setup.py and run `uv sync`
3. Create a GitHub release for the new version.

## Documentation
[TODO]
