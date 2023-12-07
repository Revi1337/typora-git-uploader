from setuptools import setup, find_packages

setup(
    name             = 'typora-git-uploader',
    version          = '1.0.0',
    description      = 'Typora Git Uploader Plugins',
    author           = 'Revi1337',
    author_email     = 'david122123@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['requests'],
	include_package_data=True,
	packages         = find_packages(),
    entry_points     = {
        'console_scripts': [
            'typora-git-uploader = typora_git_uploader.main:main'
        ]
    },
    keywords         = [
        'TYPORA UPLOADER',
        'typora uploader',
        'TYPORA GIT UPLOADER',
        'typora git uploader',
        'GIT UPLOADER',
        'git uploader'
    ],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ]
)
