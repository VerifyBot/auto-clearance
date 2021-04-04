import json
import random
import time
import os

from datetime import datetime

def get_settings(app: str = None):
  settings_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'settings.json'
  )

  if not os.path.exists(settings_path):
    raise FileNotFoundError("settings.json is missing, this file is required - download it from the repo and re-run")

  with open(settings_path, encoding="utf-8") as fp:
    js = json.load(fp)

  return js[app or "MAIN_SETTINGS"]

settings = get_settings()
LOGIN_INFO_PATH = settings["LOGIN_INFO_PATH"]
LOGS_DIR_PATH = settings["LOGS_DIR_PATH"]

def get_info(app: str = None):
  with open(LOGIN_INFO_PATH, encoding='utf-8') as fp:
    js = json.load(fp)

  return js[app] if app else js

def fill(text: str):
  for _ in range(text.count('%')):
    text = text.replace('%', str(random.randint(0, 9)), 1)
  return text


def headers(referer: str = None, extra: dict = {}):
  ver = fill('89.%.%%%%.%%%')

  headers = {
    'sec-ch-ua': '"Google Chrome";v="{0}", "Chromium";v="{0}", ";Not A Brand";v="99"'.format(ver),
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'Referer': referer,
    'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/%%%.%% (KHTML, like Gecko) Chrome/{ver} Safari/%%%.%%',
    'Content-Type': 'application/json',
    **extra
  }

  if not headers['Referer']:
    del headers['Referer']

  headers['User-Agent'] = fill(headers['User-Agent'])


  return headers

def wait(about: float, add: float = 0):
  return time.sleep(
    random.randint(-1, 1)
    * random.random()
    + about
    + random.random()
    + (add, 0)[random.randint(0, 1)])

def log(text: str, src: str = ""):
  dt = datetime.now().strftime("%x %X")

  src_text = f'[{src.upper()} @ {dt}] {text}'
  text = f'[{dt}] {text}'

  if src:
    logs_dir = [*filter(lambda path: os.path.exists(path), LOGS_DIR_PATH)][0]

    with open(os.path.join(logs_dir, f"{src}.log"), "a", encoding="utf-8") as fp:
      fp.write(f'{text}\n')

  print(src_text if src else text)

def add_file(name: str, put: str = None):
  if not os.path.exists(name):
    with open(name, "w", encoding="utf-8") as fp:
      if put:
        fp.write(put)

def add_dir(name: str):
  if not os.path.exists(name):
    os.mkdir(name)