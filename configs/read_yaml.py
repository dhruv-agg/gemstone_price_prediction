# import json
import yaml

'''
def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
'''

def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

# assert read_json("data/sample.json") == read_yaml("data/sample.yaml")
