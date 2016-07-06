import requests
url = 'https://ec2-54-145-114-189.compute-1.amazonaws.com/api/v1/job_templates/9/labels/'
payload = {
    'name': None,
    'organization': 1,
}
if __name__ == '__main__':
    for i in range(100):
        payload['name'] = 'label_{}'.format(i)
        print requests.post(url, json=payload, auth=('admin', 'uddk92hM'), verify=False, headers={'Content-Type': 'application/json'})
