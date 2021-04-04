# Auto Clearance
<p>
🎏 The goal of this project is to automatically
sign clearances in different apps / websites
</p>

## ✨ How to add a filling source
➕ add `{$appName: $appArgs}` to `login_info.json` <br>
➕ create a file named `apps/$appName.py` <br>
➕ create a function inside the file named `$appName_main` <br>
➕ add possible requirements to `requirements.txt` <br>
➕ add possible settings to `settings.json`

### 🤔 Example
<pre>
$appName="mashov"
$appArgs={"username": "XXX", "password": "XXX", "schoolID": "XXX"}
requirements: requests
settings: {"example": "XXX"}
</pre>

#### 🔍 login_info.json
```json
{
  "mashov": {
    "username": "XXX",
    "password": "XXX",
    "schoolID": "XXX"
  }
}
```

#### 🔍 apps/mashov.py
```python
def mashov_main(**kw):
  username, password, schoolID = kw.values()
  ...
```

#### 🔍 requirements.txt
```
...
requests
```

#### 🔍 settings.json
```json
"mashov": {
  "example": "XXX"
}
```