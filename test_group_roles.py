import requests
import sys
from requests.auth import HTTPBasicAuth
from pprint import pprint


def get(domain, user, password, team):
    endpoint = '/api/v1/groups/{}/'.format(team)
    response = requests.get('https://{}{}'.format(domain, endpoint),
        auth=HTTPBasicAuth(user, password), verify=False)
    print response.status_code
    if response.status_code == 403:
        return False
    for related_url in response.json()['related'].values():
        if related_url.startswith(endpoint):
            related_res = requests.get('https://{}{}'.format(domain,
                related_url), auth=HTTPBasicAuth(user, password), verify=False)
            if related_res.status_code == 403:
                return False
    return True

def ad_hoc(domain, user, password, team):
    data = """{"job_type": "run",
        "credential": null,
        "module_name": "",
        "module_args": "echo 'hey'",
        "forks": 0,
        "verbosity": 0,
        "extra_vars": "",
        "become_enabled": false,
        "inventory": null,
        "limit": ""}"""
    response = requests.post('https://{}/api/v1/groups/{}/ad_hoc_commands/'.
        format(domain, team), auth=HTTPBasicAuth(user, password), verify=False,
        data=data, headers={'Content-Type': 'application/json'})
    print response.status_code
    return response.status_code != 403

def edit(domain, user, password, team):
    data='{"description": "hehe"}'
    response = requests.patch('https://{}/api/v1/groups/{}/'.
        format(domain, team), auth=HTTPBasicAuth(user, password),
        verify=False, data=data, headers={'Content-Type': 'application/json'})
    print response.status_code
    return response.status_code != 403

def update_children(domain, user, password, team):
    data = """{"name": "fgsgsgregregesr",
        "description": "",
        "inventory": null,
        "variables": ""}"""
    response = requests.post('https://{}/api/v1/groups/{}/children/'.
        format(domain, team), auth=HTTPBasicAuth(user, password), verify=False,
        data=data, headers={'Content-Type': 'application/json'})
    print response.status_code
    return response.status_code != 403

def delete(domain, user, password, team):
    response = requests.delete('https://{}/api/v1/groups/{}/'.
        format(domain, team), auth=HTTPBasicAuth(user, password), verify=False)
    print response.status_code
    return response.status_code != 403

if __name__ == '__main__':
    print get(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print ad_hoc(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print edit(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print update_children(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print delete(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
