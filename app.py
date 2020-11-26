import requests
from requests.exceptions import ConnectionError, MissingSchema
from fastapi import FastAPI


def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    try:
        response = requests.get(hostname)
        host_status = 'up test' if response.status_code >= 100 and response.status_code < 400 else 'down test'
        return {'status': host_status}
    except ConnectionError:
        return {'status': 'down test'}
    except MissingSchema:
        return is_alive_host(f'http://{hostname}')


app = FastAPI()


@app.get('/healthz/')
def read_root(hostname):
    return is_alive_host(hostname)


#for test commit
#for test commit
#for test commit
#for test commit
#for test commit