# braglog
Easily log and manage daily work achievements to boost transparency and productivity 🌟

## Background
I got this idea from [here](https://code.dblock.org/2020/09/01/keep-a-changelog-at-work.html). My main goal is to use this project as a playground. I want to record a series of videos where we collaboratively work on solving an issue by developing a new feature each time.

## To-Do List
- [ ] Develop the `show` sub-command using a test-driven development (TDD) approach with options for `--contains`, `--from`, `--until`, and `--on`.
- [ ] Publish the app using `uv`.
- [ ] Implement the `export` functionality.
- [ ] Introduce the Ruff code formatter.
- [ ] Utilize pre-commit hooks.
- [ ] Add GitHub Actions to run test cases and check code formatting.
- [ ] Set up GitHub Actions to upload the latest version to PyPI.

## Contributing
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
