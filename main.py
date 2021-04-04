import argparse

import utils

# parse arguments
# EX: main.py --mashov
parser = argparse.ArgumentParser()

apps = utils.get_info().keys()
apps_funcs = {}

# Ugly code here we goooooo

for app in apps:
  try:
    apps_funcs[app] = getattr(__import__(f'apps.{app}', fromlist=['apps']), f'{app}_main')

    parser.add_argument(f"--{app}", default=False, action="store_true", help=f"Fill in {app}")
  except ImportError as exc:
    print(f'WARNING: {exc}')

args = parser.parse_args()

for app_name, app_func in apps_funcs.items():
  if getattr(args, app_name):
    print(f'[@] Filling clearance in {app_name}')
    app_func(**utils.get_info(app_name))