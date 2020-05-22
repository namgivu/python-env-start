# prerequisite
python 3.8 - recommended install via pyenv ref bit.ly/nnpipenv

```bash
: you@gitclonedfolder
    pyenv install 3.8.2 ; pyenv global 3.8.2 ; python -V ; should_see='Python 3.8.2'
    # install             set global           view version

    python -m pip install --upgrade pip ; python -m pip install pipenv ; pipenv --version  ; should_see='pipenv, version 2018.11.26'
    # update most-recent pip              isntall pipenv                 view version      
```

# install package
```bash
: you@gitclonedfolder
    pipenv sync ; pipenv --venv ; should_see='/path/to/:gitclonedfolder/.venv/'
```

# demo env
```bash
pipenv run python src/demo_env.py
```
