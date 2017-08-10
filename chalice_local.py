import os

from chalice import cli
from chalice.cli.factory import CLIFactory


project_dir = os.getcwd()
obj = dict()
obj['project_dir'] = project_dir
obj['debug'] = True
obj['factory'] = CLIFactory(project_dir, True)


cli.local([], obj=obj)