import os

PV_INDEPENDENCE_PREMCALC_URL=os.environ.get('PV_INDEPENDENCE_PREMCALC_URL')

if PV_INDEPENDENCE_PREMCALC_URL is None: raise Exception('Not found PV_INDEPENDENCE_PREMCALC_URL in .env file - clone one from ./docker/config_vault/xxx/.env to :gitclonedfolder/.env')

print(f'''
Python code sending request to endpoint at :PV_INDEPENDENCE_PREMCALC_URL here
$ http POST PV_INDEPENDENCE_PREMCALC_URL
$ http POST {PV_INDEPENDENCE_PREMCALC_URL}
''')
