import os
import argparse
import json
from json import JSONDecodeError
import requests
import base64
import sys


if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG = os.path.join(BASE_DIR, 'config.json')
SNIPPETS = {
    "github": {
        "username": "",
        "repo": "",
        "token": "",
        "branch": ""
    }
}

def configuration_properties(arguments: dict) -> dict:

    """ configuration properties via input arguments """

    with open(CONFIG, 'r') as f:
        properties = json.load(f)
        github_properties = properties['github']
        if isinstance(github_properties, dict):
            for argument in arguments:
                if arguments[argument] is None or argument == 'upload':
                    continue
                github_properties[argument] = arguments[argument]
    with open(CONFIG, 'w') as f:
        json.dump(properties, f)
    return github_properties



def upload_image(properties: dict, file_meta_data: list = None) -> dict:

    """ request to github api for file upload """

    if file_meta_data is None:
        meta_data = properties['upload']
    else:
        meta_data = file_meta_data[::-1]
    body, headers, url = build_web_components(properties, meta_data)
    with requests.put(url, headers=headers, json=body) as res:
        res.raise_for_status()
    return res.json()



def build_web_components(github_properties: dict, file_meta_data: list) -> tuple[dict, dict, str]:

    """ build web components for request github (url, body, headers) """

    remote_upload_dir, local_uploaded_path = file_meta_data
    user_repository = "/".join([github_properties['username'], github_properties['repo']])
    fully_upload_path = "/".join([remote_upload_dir, os.path.basename(local_uploaded_path)])

    url = f"https://api.github.com/repos/{user_repository}/contents/{fully_upload_path}"
    headers = {
        "Authorization": f"Bearer {github_properties['token']}",
        "Accept": "application/vnd.github+json"
    }
    with open(local_uploaded_path, 'rb') as image:
        body = {
            "message": "auto upload from revi1337 plugins api",
            "content": base64.b64encode(image.read()).decode('utf8'),
            "branch": github_properties['branch']
        }
    return body, headers, url



def initialize() -> None:

    """ if initialize config.json snippets """

    with open(CONFIG, 'a') as f:
        json.dump(SNIPPETS, f)



def parse_arguments() -> dict:

    """ parse command line arguments """

    parser = argparse.ArgumentParser()
    parser.add_argument('--username',  help='github username')
    parser.add_argument('--repo', help='github repo expected to be uploaded')
    parser.add_argument('--token', help='github token required to upload')
    parser.add_argument('--branch', help='github repo branch expected to be uploaded')
    parser.add_argument('--upload', nargs=2, metavar=('remote_upload_dir', 'local_uploaded_path'), help='remote_upload_dir and local_uploaded_path')
    return parser.parse_args().__dict__



def parse_configuration() -> json:

    """ parse config.json and get github properties """

    with open(CONFIG, 'r') as f:
        try:
            json_value = json.load(f)
        except JSONDecodeError:
            raise ValueError("config.json has invalid json format")
    return json_value['github']


def main():

    """ main function this function called by setup.py entry_points """

    arguments = parse_arguments()
    active_options = list(
        filter(lambda argument: arguments[argument], arguments)
    )
    if len(active_options) == len(arguments):
        response = upload_image(arguments)
        print(response['content']['download_url'])
    elif arguments['upload'] and len(active_options) == 1:
        configuration = parse_configuration()
        github_properties = configuration_properties(arguments)
        response = upload_image(github_properties, arguments['upload'])
        print(response['content']['download_url'])
    else:
        if not os.path.exists(CONFIG):
            initialize()
        parse_configuration()
        configuration_properties(arguments)


if __name__ == '__main__':
    main()
