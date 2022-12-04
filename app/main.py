import json
from urllib.request import urlopen as url_open
from urllib.request import Request as url_request

from logger import log

def download(self, url):
    
    request = self.make_url_request(url)
    
    with url_open(request) as response:
        response_data = response.read()
    
    return response_data


def make_url_request(self, url):
    return url_request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
        }
    )


def get_device_verification_code(client_id):
    request = url_request(
        'https://github.com/login/device/code', 
        data=json.dumps({
            'client_id' : client_id,
        }).encode('utf-8'), 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, method='POST')

    with url_open(request) as response:
        response_data = response.read()
    
    return json.loads(response_data.decode("utf-8"))


def get_access_token(client_id, device_code):
    request = url_request(
        'https://github.com/login/oauth/access_token', 
        data=json.dumps({
            'client_id' : client_id,
            'device_code': device_code,
            'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'
        }).encode('utf-8'), 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            "Content-Type": "application/json",
            "Accept": "application/json"
        }, method='POST')

    with url_open(request) as response:
        response_data = response.read()
    
    print(response_data)
    return json.loads(response_data.decode("utf-8"))


def get_authenticated_user(access_token):
    request = url_request(
        'https://api.github.com/user', 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {access_token}"
        })

    with url_open(request) as response:
        response_data = response.read()
    
    print(response_data)
    return json.loads(response_data.decode("utf-8"))


def get_public_repositories(access_token):
    request = url_request(
        'https://api.github.com/repositories', 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {access_token}"
        })

    with url_open(request) as response:
        response_data = response.read()
    
    print(response_data)
    return json.loads(response_data.decode("utf-8"))


if __name__ == "__main__":

    # log = setup_logging()

    output_path = '../output'

    client_id = 'f2d...'
    device_code = 'f71...'
    access_token = "gho..."

    pat_access_token = "github..."

    # get_authenticated_user(access_token)
    # get_public_repositories(access_token)
    
    log.info("Program complete", source="program", event="complete")

