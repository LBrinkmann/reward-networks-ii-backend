# Python App Template

Python version >= 3.7 is required.

## Setup

```
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install -e ".[dev]"
```

## Run Locally

```
export NETWORK_FILE="$(PWD)/app/data/test.json"
export RN_FRONTEND="$(PWD)/../reward-networks-ii-frontend"

./dev_server.sh
```

## Visualize Data Model

Install graphviz https://graphviz.org/download/

Install pygraphviz

```
pip install --global-option=build_ext --global-option="-IC:/usr/local/include/" --global-option="-LC:/usr/local/lib/" pygraphviz
```

Install erdantic

```
pip install erdantic
```

Run design/diagram.ipynb

## Deployment

### Logs

https://onenr.io/0EPwJ0NDkj7
