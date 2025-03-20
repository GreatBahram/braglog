# braglog
Easily log and manage daily work achievements to boost transparency and productivity 🌟

## Background
I got this idea from [here](https://code.dblock.org/2020/09/01/keep-a-changelog-at-work.html). My main goal is to use this project as a playground. I want to record a series of videos where we collaboratively work on solving an issue by developing a new feature each time.

## To-Do List
- [x] Develop the `show` sub-command using a test-driven development (TDD) approach with options for `--contains`, `--from`, `--until`, and `--on`.
- [ ] Publish the app using `uv`.
- [ ] Implement the `export` functionality.
- [ ] Introduce the Ruff code formatter.
- [ ] Utilize pre-commit hooks.
- [ ] Add GitHub Actions to run test cases and check code formatting.
- [ ] Set up GitHub Actions to upload the latest version to PyPI.

## Usage

For help, run:
```bash
braglog --help
```
You can also use:
```bash
python -m braglog --help
```
### Adding Work Achievements

To log today's achievement:
```bash
braglog Fixed the authentication bug in login module
```

To log an achievement for a specific date:
```bash
braglog --date 2025-03-19 "Completed code review for PR #123"
```

To see the location of your logs file:
```bash
braglog logs-path
```
### Viewing Work Achievements

View all entries or filter them:
```bash
# Show all entries
braglog show

# Filter by text
braglog show --contains "bug fix"

# Show entries for specific date
braglog show --on "2025-03-19"

# Quick manager meeting prep - show last 2 weeks of achievements
braglog show -s "2 weeks ago"
```
> [!NOTE]
> `--on` cannot be used with `--since` or `--until`
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
To run the tests:
```
uv run pytest .
```