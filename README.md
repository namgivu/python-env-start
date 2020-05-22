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
: you@gitclonedfolder
    pipenv run python src/demo_env.py
        should_see='
        Loading .env environment variables…
        some value
        '
        #NOTE: the .env file is auto-loaded 

    # run without pipenv run i.e. directly call python binary 
    ./.venv/bin/python src/demo_env.py
    # python binary    py file to run
        result='
        None
        '
    
    # run with env var as prefix to the command 
    SOME_VAR='vvv'        ./.venv/bin/python src/demo_env.py
    # env var as prefix   python binary    py file to run
        result='
        vvv
        '
    
    # with env var(s) in .env 
    eval "`cat ./.env`"      ./.venv/bin/python src/demo_env.py
    # load .env as env var   python binary      py file to run
        result='
        some value
        '
```

So here is the conclusion

00 from pyton code, `os.environ` is where to get them e.g. os.environ.get('SOME_VAR') or os.environ['SOME_VAR']

01a env var can be defined as command prefix
01b env var can be defined in .env and loaded as command prefix manually

01b env var can be defined in .env and auto-loaded with `pipenv run`

02 how about not using `pipenv run` ? we can autoload via [python-dotenv package](https://pypi.org/project/python-dotenv/)


# demo Siri-context .env usage

## use UAT .env 
```bash
: you@gitclonedfolder
    cp ./docker/config_vault/UAT/app_config/.env   ./.env
    #  UAT .env file                               app .env file

    pipenv run python ./src/product/PV_Independence/PremiumHandler.py   
        should_see='
        Loading .env environment variables…
        
        Python code sending request to endpoint at :PV_INDEPENDENCE_PREMCALC_URL here
        $ http POST PV_INDEPENDENCE_PREMCALC_URL
        $ http POST http://68.183.235.218:20326/premium_calculator
        '
```

