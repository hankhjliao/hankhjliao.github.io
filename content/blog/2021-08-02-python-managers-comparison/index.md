---
Title: Python Managers Comparison
Date: 2021-08-02T11:20:00
# Categories: Python
Tags: [python, comparison]
Slug: 2021-08-02-python-managers-comparison
Summary: Python managers comparison
---

{{<notice note>}}
For Windows user / machine learning / newbie: Recommend to use conda + pip
{{</notice>}}

## Manage Python interpreter version

### conda

Installation: https://docs.conda.io/en/latest/miniconda.html
Specify the Python version when creating the environment: `conda create -n env python=3.8`

### pyenv

Installation:
- Mac: https://github.com/pyenv/pyenv#installation
- Linux: https://github.com/pyenv/pyenv-installer
- Windwos: https://github.com/pyenv-win/pyenv-win

Install a new version: `pyenv install -v 3.8.0`
Set the global version: `pyenv global 3.8.0`
Set the local version: `pyenv local 3.8.0`
List versions: ` pyenv versions`

## Manage Python virtual environment

### Global

|                | virtualenvwrapper                        | conda                                |
| -------------- | ---------------------------------------- | ------------------------------------ |
| Installation   | pip install virtualenv virtualenvwrapper | [^conda_install]                     |
| Env List       | lsvirtualenv                             | conda env list                       |
| Env Create     | mkvirtualenv `env`                       | conda create -n `env`                |
| Env Activate   | workon `env`                             | conda activate `env`                 |
| Env Deactivate | deactivate                               | conda deactivate                     |
| Env Remove     | rmvirtualenv `env`                       | conda env remove -n `env`            |
| Env Duplicate  | cpvirtualenv `orig` `new`                | conda create -n `new` --clone `orig` |

#### Virtualenvwrapper setup

```sh
# In .bashrc/.profile/.zshrc etc.
export WORKON_HOME=<path-to-env-stored>
export VIRTUALENVWRAPPER_PYTHON= $(which python3)
source /usr/local/bin/virtualenvwrapper.sh
```

### Local

|                | venv                      | virtualenv                | conda                     | pipenv                           | poetry                    |
| -------------- | ------------------------- | ------------------------- | ------------------------- | -------------------------------- | ------------------------- |
| Installation   | -                         | pip install virtualenv    | [^conda_install]          | [^pipenv_install]                | [^poetry_install]         |
| Env Create     | python -m venv `env`      | virtualenv `env`          | conda create -p `env`     | pipenv --python `python-version` | poetry init               |
| Env Activate   | source `env`/bin/activate | source `env`/bin/activate | conda activate ./`env`    | pipenv shell                     | poerty shell              |
| Env Deactivate | deactivate                | deactivate                | conda deactivate          | ++ctrl+d++                       | ++ctrl+d++                |
| Env Remove     | Delete `env` folder       | Delete `env` folder       | conda env remove -p `env` | pipenv --rm                      | [^poetry_remove_env]      |
| Env Run        | -                         | -                         | -                         | pipenv run python main.py        | poetry run python main.py |

## Manage python packages

|                 | pip                             | conda                               | pipenv                             | poetry                                                |
| --------------- | ------------------------------- | ----------------------------------- | ---------------------------------- | ----------------------------------------------------- |
| Installation    | [^pip_install]                  | [^conda_install]                    | [^pipenv_install]                  | [^poetry_install]                                     |
| Package Install | pip install `pkg`               | conda install `pkg`                 | pipenv install `pkg`               | poetry add `pkg`                                      |
| Package Update  | pip install --upgrade `pkg`     | conda update `pkg`                  | pipenv update `pkg`                | poetry update `pkg`                                   |
| Package Remove  | pip uninstall `pkg`             | conda remove `pkg`                  | pipenv uninstall `pkg`             | poetry remove `pkg`                                   |
| Env Export      | pip freeze > requirements.txt   | conda env export > environment.yml  | Pipfile                            | pyproject.toml                                        |
| Env Deploy      | pip install -r requirements.txt | conda env create -f environment.yml | pipenv install                     | poetry install                                        |
| Import from pip | -                               | [^conda_import_pip]                 | pipenv install -r requirements.txt | [^poetry_import_pip]                                  |
| Export to pip   | -                               | -                                   | pipenv lock -r > requirements.txt  | poetry export -f requirements.txt -o requirements.txt |

### pip

1. Install packages from [PyPI](https://pypi.org/).
2. Won't remove dependencies when removing explicitly installed packages.
   (Solution: `pip install python3-pip-autoremove`, `pip3-autoremove <pkg>`)
3. Visualize dependencies in `requirements.txt`:
    1. `pip install pipdeptree`
    2. `pipdeptree -f > requirements.txt`
4. Mimic separating development env and production env.
    1. [Without any tools](https://stackoverflow.com/a/20720019)
    2. [Using pip-tools](https://stackoverflow.com/a/65908367)

### conda

1. Install packages from [Anaconda](https://anaconda.org/), which has fewer packages than [PyPI](https://pypi.org/).
2. Can use pip/poetry inside conda env.
   (Set `poetry config settings.virtualenvs.create false` when using poetry inside conda env)
3. Support nested env activation: `conda activate --stack <env>`
4. For exporting packages which is explicitly installed with **conda**: `conda env export --from-history`

### pipenv

1. Install packages from [PyPI](https://pypi.org/).
2. Support separating development env and production env.
   1. Package Install: `pipenv install <pkg> --dev`
   2. Env Deploy: `pipenv install --dev`
3. Support `.env` file.
4. Generating `Pipfile.lock` is time-consuming.

### poetry

1. Install packages from [PyPI](https://pypi.org/).
2. Support separating development env and production env.
   1. Package Install: `poetry add <pkg> --dev`
   2. Package Remove: `poetry remove <pkg> --dev`
   3. Env Deploy: `poetry install --no-dev`
3. It is hard to type poetry fast. :smile:

## Reference

- https://docs.conda.io/projects/conda/en/latest/index.html
- https://github.com/pyenv/pyenv
- https://virtualenvwrapper.readthedocs.io/en/latest/
- https://virtualenv.pypa.io/en/latest/
- https://pip.pypa.io/en/stable/getting-started/
- https://pipenv.pypa.io/en/latest/
- https://python-poetry.org/
- https://stackoverflow.com/questions/17803829/how-to-customize-a-requirements-txt-for-multiple-environments
- https://stackoverflow.com/questions/47311847/separating-development-and-production-dependencies-with-virtualenv
- https://stackoverflow.com/questions/35802939/install-only-available-packages-using-conda-install-yes-file-requirements-t
- https://stackoverflow.com/questions/62764148/how-to-import-requirements-txt-from-an-existing-project-using-poetry

<!-- footnote -->
[^pip_install]: Use system package manager (e.g. `apt`, `yum`) or `curl -sSL https://bootstrap.pypa.io/get-pip.py | python`
[^conda_install]: https://docs.conda.io/en/latest/miniconda.html
[^pipenv_install]: `pip install pipenv` or `curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python`
[^poetry_install]: `curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python`
[^conda_import_pip]: `while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt`
[^poetry_import_pip]: `cat requirements.txt | xargs poetry add`
[^poetry_remove_env]: `poetry env list --full-path`, `poetry env remove <env>`
