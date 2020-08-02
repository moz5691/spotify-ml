# spotify-ml

# Instruction

## Download datafile and store in data folder at root level.

## Using CLI (no docker)

- Mac/Linux

```
$ python3 -m venv env
$ source env/bin/activate
$ pip install requirements.txt

(env)$ export FLASK_APP=project/__init__.py
(env)$ export FLASK_ENV=development
(env)$ python manage.py run
```

- Win

```
> pip install requirements.txt
> set FLASK_APP = "project/__init__.py"
> set FLASK_ENV = "development"
> python manage.py
```

## Using DOCKER (tbd)

---

### To run Open API page (SWagger)

- Open browser, `http://localhost:3000/doc`

### Folder structure

- project/api/models <-- Create model and scaler using Jupyter notebook and move them to this folder
- project/api/pred_popularity <-- views and crud for popularity prediction
- project/api/pred_danceability <-- views and crud for danceability prediction
