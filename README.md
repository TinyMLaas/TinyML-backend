# TinyML-backend

backend for [TinyMLaaS](https://github.com/JeHugawa/TinyMLaaS-main/).

## Virtualenvironment

To activate virtualenvironment, run

```
source venv/bin/activate
```

## Run app

In order to run app, be in the virtualenvironment. Then, in the root directory, run

```
uvicorn main:app --reload
```

## Dependencies

In requirements.txt. Install them with pip install -r requirements.txt

## Testing

Run unit tests with

```
python -m unittest discover -v
```
