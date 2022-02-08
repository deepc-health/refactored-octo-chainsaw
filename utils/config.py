import yaml
def read_yaml(config_path):
    with open(config_path, "r") as stream:
        config = yaml.full_load(stream)

    return config


config_path = f"./config.yaml"
config = read_yaml(config_path)
