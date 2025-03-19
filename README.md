
## Contributing
To contribute to this tool, first checkout the code. Then create a new virtual environment:
```shell
cd logit
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
