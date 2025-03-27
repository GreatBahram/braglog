# braglog
Easily log and manage daily work achievements to boost transparency and productivity 🌟

## Background
I got this idea from [here](https://code.dblock.org/2020/09/01/keep-a-changelog-at-work.html). My main goal is to use this project as a playground. I want to record a series of videos where we collaboratively work on solving an issue by developing a new feature each time.

## To-Do List
- [x] Develop the `show` sub-command using a test-driven development (TDD) approach with options for `--contains`, `--from`, `--until`, and `--on`.
- [x] Publish the app using `uv`.
- [x] Introduce the Ruff code formatter.
- [x] Utilize pre-commit hooks.
- [x] Add GitHub Actions to run test cases and check code formatting.
- [x] Set up GitHub Actions to upload the latest version to PyPI.
- [ ] Implement the `export` functionality.
## Installation
Install this tool using pip:
```bash
pip install braglog
```
Or using [pipx](https://pipx.pypa.io/stable/):
```bash
pipx install braglog
```
Or using [uv](https://docs.astral.sh/uv/guides/tools/):
```bash
uv tool install braglog
```
## Usage

For help, run:
```bash
braglog --help
```
You can also use:
```bash
python -m braglog --help
```
