# typora-git-uploader

Plugins for `Typora` to Upload Image Automatically to Remote Repository

## Table of Contents

  * [Installation](#installation)
  * [Usage](#Usage)
  * [Quick start](#quick-start)
  * [Features](#features)
  
## Installation

Download using pip via PYPI.

```bash
$ pip install typora-git-uploader
```

or 

Download using git.

```bash
$ git clone https://github.com/Revi1337/typora-git-uploader.git
$ cd typora-git-uploader
$ python setup.py install
```

## Usage

```bash
$ typora-git-uploader -h
usage: typora-git-uploader [-h] [--username USERNAME] [--repo REPO] [--token TOKEN] [--branch BRANCH] [--upload remote_upload_dir local_uploaded_path]
options:
  -h, --help            show this help message and exit
  --username USERNAME   github username
  --repo REPO           github repo expected to be uploaded
  --token TOKEN         github token required to upload
  --branch BRANCH       github repo branch expected to be uploaded
  --upload remote_upload_dir local_uploaded_path
                        remote_upload_dir and local_uploaded_path
```

## Quick start

```bash
$ typora-git-uploader 
      --username=USERNAME --repo=REPOSITORY --token=API_TOKEN 
      --branch=BRANCH --upload EXPECTED_REMOTE_PATH LOCAL_UPLOADED_PATH     
```

Change `Custom Command` and specify `typora-git-uploader` commnad in `Typora Image Settings`


![image](https://github.com/Revi1337/BlogImageFactory/assets/86167726/d6384472-945e-4ada-9bfa-0daffdcb4b29)

When you paste image in you typora editor, you can see the uploaded path seems to be in local directory.

![image](https://github.com/Revi1337/BlogImageFactory/assets/86167726/a171bf05-876c-4d9a-887f-1903c622bfcc)

after when you click `Image Upload` in typora editor, Typora trigger our `typora-git-uploader` and upload image to remote repostiory.
so you can see the uploaded path seems to be in remote address.
That means our `command` works correct.

![image](https://github.com/Revi1337/BlogImageFactory/assets/86167726/55fa31c1-588c-421f-a27c-64a8410f4e92)

## Features

  * `Typora` Plugins for Uploading Files to Git
