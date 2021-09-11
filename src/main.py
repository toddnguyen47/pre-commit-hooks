from read_in_yaml_config import read_in_yaml_config
from convert_beginning_tabs import ConvertBeginningTabs

import os

from collections import namedtuple

_CONFIG_YAML = "config.yaml"
ConfigTuple = namedtuple("Config", ["dir_path", "num_spaces", "extension"])


def get_config() -> ConfigTuple:
    current_dir = read_in_yaml_config.get_current_file_dir(__file__)
    config_file = os.path.join(current_dir, _CONFIG_YAML)
    yaml_config_dict = read_in_yaml_config.read(config_file)
    dir_path = yaml_config_dict["directory-path"]
    num_spaces = yaml_config_dict["num-spaces"]
    extension = yaml_config_dict["extension"]
    return ConfigTuple(dir_path, num_spaces, extension)


if __name__ == "__main__":
    convert_beginning_tabs = ConvertBeginningTabs()
    config_tuple = get_config()
    convert_beginning_tabs.convert_on_files_with_ext(
        config_tuple.dir_path, config_tuple.num_spaces, config_tuple.extension
    )
