# spotify-ml

# Instruction

## Download datafile and store in data folder at root level.

https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db/data#

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
> python manage.py run
```

## Using DOCKER

```
  # build and run docker container
  $ docker-compose up -d --build
  # check if it runs with no errors
  $ docker-compose logs
```

## Deployment

```
$ heroku create
Creating app... done, ⬢ mighty-eyrie-17457

$ heroku container:login
$ docker build -f Dockerfile.prod -t registry.heroku.com/mighty-eyrie-17457/web .
$ docker push registry.heroku.com/mighty-eyrie-17457/web:latest
$ heroku container:release web -a mighty-eyrie-17457
```

### To run Open API page (Swagger)

- Open browser, For CLI, `http://localhost:5000/doc`
  For Docker, `http://localhost:5001/doc`
- refer "Models" section for Input data types and format

### Folder structure

- project/api/api_models <-- Create model and scaler using Jupyter notebook and move them to this folder
- project/api/pred_popularity <-- views and crud for popularity prediction
- project/api/pred_danceability <-- views and crud for danceability prediction
