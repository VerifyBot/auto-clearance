import requests
import json

from datetime import datetime

import utils

def mashov_main(**kw):
  username, password, schoolID = kw.values()

  default_headers = utils.headers(referer="https://web.mashov.info/students/login")

  session = requests.Session()

  # login
  resp = session.post(
    url="https://web.mashov.info/api/login",
    headers=default_headers,
    data=json.dumps(dict(
      username=username,
      password=password,
      semel=schoolID,
      year=datetime.now().year,
      appName="info.mashov.students"
    )))

  csrf_token = resp.cookies.get('Csrf-Token')
  login_js = resp.json()

  utils.log(f'Logged in as {login_js["accessToken"]["displayName"]}', src="mashov")

  date = datetime.utcnow().isoformat().split('.')[0]

  for student in login_js['accessToken']['children']:
    utils.wait(2, add=2)
    resp = session.put(
      url="https://web.mashov.info/api/students/{0}/covid/{1}Z/clearance".format(student['childGuid'], date),
      headers={**default_headers, "Referer": "https://web.mashov.info/students/main/covidClearance", "X-Csrf-Token": csrf_token},
      data=json.dumps(dict(
        answer=3,
        answererName=login_js["accessToken"]["displayName"],
        answererId=login_js["credential"]["userId"],
        clearanceDate=date,
        lastAnswer=date,
        lastAnswerIsOk=True,
        studentClass='{classCode} {classNum}'.format_map(student),
        studentName='{privateName} {familyName}'.format_map(student),
        userId=student['childGuid'],
        noContactWithInfected=True,
        noHeatAndSymptoms=True,
      ))
    )

    if resp.ok:
      utils.log(f'The clearance was successfully signed for {student["privateName"]}', src="mashov")
    else:
      utils.log(f'Signature the clearance for {student["privateName"]} failed', src="mashov")