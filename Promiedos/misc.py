import yaml
import sys

def read_cfg_yaml(file):
    with open(file, 'r') as file:
        return yaml.safe_load(file)

def set_yaml_file():
    return sys.argv[0][:-3]+".yaml"