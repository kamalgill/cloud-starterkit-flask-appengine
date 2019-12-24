# Starter Kit for Flask on Google App Engine

Starter project template for running a Flask-based application on
Google App Engine Standard Python 3 Runtime.

The application structure of this starter kit is loosely inspired by Miguel Grinberg's 
[Flask Web Development (Second Edition)](http://oreilly.com/catalog/0636920089056) book,
with the book's companion repo at https://github.com/miguelgrinberg/flasky


## Development Setup Requirements

- Python 3.7 or later
- Windows, MacOS, and Linux development environments are supported


## Development Setup Instructions

Assuming the development setup requirements above have been satisfied,
run the following in a terminal (git-bash is recommended on Windows) after cloning the repo
to set up your local development environment.

```bash 
# Install local dev requirements, ideally in an isolated Python 3.7 (or later) environment
pip install -r requirements-dev.txt
```


## Running the Development Server

If you're on Linux or MacOS you can run the app via `gunicorn`, which offers a `--reload` option and
more closely emulates the App Engine production runtime, which uses gunicorn by default.

```bash
# Linux and MacOS only, use --reload flag to automatically reload on code changes
gunicorn --reload app:application
```

```bash
# Cross-platform -- works on Windows, MacOS and Linux, albeit without a --reload option
waitress-serve app:application
```

The app is viewable at http://localhost:8000 (for gunicorn) or at http://localhost:8080 (for Waitress).

The sample hello endpoint is at /api/v1/hello/world


### Customizing the HTTP Port

The app runs on port 8000 (for gunicorn) and 8080 (for waitress) by default.  

To customize the port, pass the `--port` option as in the following example...

```bash
# Set gunicorn port to 9000
gunicorn --port=9000 --reload app:application

# Set Waitress port to 9000
waitress-serve --port=9000 app:application
```

## Running Tests

The tests are run via `pytest`, with the configuration file at `pytest.ini`.

```bash
# Run all tests
pytest

# Run only a particular test
pytest tests/test_api.py::test_hello

```


## Google Cloud Setup Instructions

1. Create an App Engine Project at https://console.cloud.google.com/appengine
2. Download and install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
3. Run the "Google Cloud SDK Shell" application
4. Type `gcloud init` in the Cloud SDK Shell
5. Set the active project (created in step 1) in the Cloud SDK Shell via `gcloud config set project PROJECT_ID`
5. Install the App Engine components in the Cloud SDK Shell via `gcloud components install app-engine-python`
6. Log in via `gcloud auth login` in the Cloud SDK Shell


## Deploying to Google App Engine

Run the following command at the repo root (where the `app.yaml` config file is located) to deploy to App Engine...

```bash
# Deploy to App Engine
gcloud app deploy
```
