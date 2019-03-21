import os
import subprocess
from typing import List

from setuptools import (
    setup,
    Command,
)

PACKAGE_NAME = 'dmm-reminder'


class SimpleCommand(Command):
    user_options: List = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class VetCommand(SimpleCommand):
    def run(self):
        subprocess.run(['mypy', 'main.py'])
        subprocess.run(['flake8'])


class FmtCommand(SimpleCommand):
    def run(self):
        subprocess.run(['isort', '-y'])
        subprocess.run(['autopep8', '-ivr', 'main.py', 'tests', 'setup.py'])


class TestCommand(SimpleCommand):
    def run(self):
        subprocess.run(['mypy', 'main.py'])
        subprocess.run(['flake8'])
        subprocess.run(['tox'])


class DeployCommand(SimpleCommand):
    def run(self):
        with open('requirements.txt', 'w') as outfile:
            subprocess.run(['pipenv', 'lock', '-r'], stdout=outfile)
        subprocess.run(['gcloud', 'config', 'set', 'project', os.environ['PROJECT_ID']])
        subprocess.run(['gcloud', 'functions', 'deploy', os.environ['FUNCTION_NAME'],
                        '--runtime', 'python37',
                        '--region', 'asia-northeast1',
                        '--trigger-http'])
        os.remove('requirements.txt')


setup(
    # metadata
    name=PACKAGE_NAME,
    version='0.1.0',
    # options
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    # https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-list
    cmdclass=dict(
        vet=VetCommand,
        fmt=FmtCommand,
        test=TestCommand,
        deploy=DeployCommand,
    )
)
