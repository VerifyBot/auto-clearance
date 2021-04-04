import os
import pip

import utils

# add missing modules
with open("requirements.txt") as fp:
  modules = [*filter(bool, fp.readlines())]

for module in modules:
  try:
    __import__(module)
  except ImportError:
    pip.main(["install", "-U", module])

# add missing files & directories
utils.add_file('login_info.json', '{}')
utils.add_dir('./logs')
utils.add_dir('./apps')