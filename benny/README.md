**Setup virtual env (only first time cloning)**
```
pip install virtualenv
virtualenv -p "PYTHONPATH" venv
```

**Activate virtual env from the source**
```
.\venv\Scripts\activate
```

**Put all current packages in the requirements.txt**
```
pip freeze > requirements.txt
```

**Install all requirements from the requirements.txt**
```
pip install -r requirements.txt
```
