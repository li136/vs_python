import argparse, yaml
from cfgs.base_cfgs import Cfgs


cfg_file = "mcan-vqa-master\cfgs\small_model.yml"

__C = Cfgs()

with open(cfg_file, 'r') as f:
    yaml_dict = yaml.safe_load(f)
print(yaml_dict)
args_dict = {**yaml_dict, **__C}