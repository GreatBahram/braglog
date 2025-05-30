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
## Environment Variables
The application uses the following environment variable:

- **`BRAGLOG_CONFIG_DIR`**: Specifies the directory where the application's configuration and database files are stored. If not set, the default directory will be used (typically a platform-specific application directory).

To set this environment variable, use the following command:

```shell
export BRAGLOG_CONFIG_DIR=.
```
## Release process
To release a new version:

1. Create a new branch like `v0.5.0`
2. Update `docs/changelog.md` with the new changes.
3. Update the version number in `setup.py` and run `uv sync`.
4. Create a git tag: `git tag v0.5.0`.
5. Create a GitHub release for the new version using the tag


## Documentation
The documentation is built using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

### Setting up documentation locally
1. Make sure you've installed the development dependencies as mentioned above.
2. Run the following command to start a local documentation server:

```shell
mkdocs serve
```
