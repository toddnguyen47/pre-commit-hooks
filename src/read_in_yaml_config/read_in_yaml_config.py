import yaml

import os


def get_current_file_dir(file_path: str):
    return os.path.dirname(os.path.realpath(file_path))


def read(config_file: str) -> dict:
    with open(config_file) as file:
        yaml_file = yaml.safe_load(file)
    return yaml_file


if __name__ == "__main__":
    current_dir = get_current_file_dir(__file__)
    config_file = os.path.join(current_dir, "config.yaml")
    yaml_dict = read(config_file)
    print(yaml_dict)
