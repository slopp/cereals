# This file allows you to run dagit using the default
# workspace.yaml
# Alternatively, you can omit this file and run: 
#
# dagit -f cereal_project/repository.py
#
# Or modify the workspace.yaml file to have:
#
# load_from:
#    - python_file: cereal_project/repository.py
#
# Any changes to workspace.yaml should also be made to 
# dagster_cloud.yaml

from .repository import cereal_project, cereal_project2