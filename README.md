# Starter Kit for Flask on Google App Engine

Starter project template for running a Flask-based application as a Web API on
Google App Engine Standard (Python 3.7 Runtime).

The application structure of this starter kit is loosely inspired by the API chapter of Miguel Grinberg's 
[Flask Web Development (Second Edition)](http://oreilly.com/catalog/0636920089056) book,
with the companion repo at https://github.com/miguelgrinberg/flasky


## Scope of this starter kit

The scope of this starter kit is fairly small, punting on the front-end UI implementation
to avoid bloating the code and keeping the list of opinionated choices fairly minimal.

### In scope and already implemented

This starter kit includes the following:

- Minimal Flask API blueprint, with a sample "hello world" handler at `app/api/hello.py`
- Production-ready App Engine configuration (in `app.yaml`) with Flask WSGI app running via gunicorn and gevent
- Continuous Integration (CI) workflow via GitHub Actions (see `.github/workflows/continous-integration.yaml`)
- Unit tests via pytest (see `tests/test_api.py`)

### Not yet implemented

The starter kit does not yet include the following (PRs are welcome):

- Continous deployment (CD) workflow via GitHub Actions, leveraging https://github.com/GoogleCloudPlatform/github-actions
- Acceptance/smoke tests hitting API endpoints on App Engine post-deployment
- Sample integration with Cloud Firestore
- Sample auth integration


## Development Setup Requirements

- Python 3.7 or later
- Windows, macOS, and Linux development environments are supported


## Development Setup Instructions

Assuming the development setup requirements above have been satisfied,
run the following in a terminal (git-bash is recommended on Windows) after cloning the repo
to set up your local development environment.

```bash 
# Install local dev requirements, ideally in an isolated Python 3.7 (or later) environment
pip install -r requirements-dev.txt
```


## Running the Development Server

If you're on Linux or macOS you can run the app via `gunicorn`, which offers a `--reload` option and
more closely emulates the App Engine production runtime, which uses gunicorn by default.

```bash
# Linux and macOS only, use --reload flag to automatically reload on code changes
gunicorn app:application --reload
```

```bash
# Cross-platform, works on Windows, macOS and Linux, albeit without a --reload option available
waitress-serve app:application
```

The app is viewable at http://localhost:8000 (for gunicorn) or at http://localhost:8080 (for Waitress).

The sample hello endpoint is at `http://$HOST:$PORT/api/v1/hello/world`

### Customizing the HTTP Port

The app runs on port 8000 (for gunicorn) and 8080 (for waitress) by default.  

To customize the port, pass the `--bind` option (for gunicorn) 
or the `--port` option (for Waitress) as in the following examples...

```bash
# Set gunicorn port to 9000
gunicorn --bind=:9000 app:application --reload

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

The following steps only need to be performed once per local development environment...

1. Create an App Engine Project at https://console.cloud.google.com/appengine
2. Download and install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
3. If on Windows, run the "Google Cloud SDK Shell" application
4. Type `gcloud init` in a terminal or in the Cloud SDK Shell
5. Log in via `gcloud auth login` in a terminal or in Cloud SDK Shell as needed
6. Set the active project (created in step 1) via `gcloud config set project PROJECT_ID`
7. If on Windows or macOS, install the App Engine components via `gcloud components install app-engine-python`


## Deploying to Google App Engine

Ensure the project you want to deploy is selected via `gcloud config set project PROJECT_ID`, then
run the following command at the repo root (where the `app.yaml` config file is located) to deploy to App Engine...

```bash
# Deploy to App Engine
gcloud app deploy
```


## CI/CD

A GitHub Actions continuous integration (CI) workflow is provided in the `.github/workflows` folder, running
unit tests when a non-master branch is pushed to GitHub.

Perform the following steps to configure the CI workflow to be enforced on GitHub pull requests (PRs) against
the repo's master branch:

1. In the GitHub UI for your forked repo, click the `Settings` tab at top and click the `Branches` nav item at left.
2. In the `Branch protection rules` section, click the `Add rule` button if there is no rule for the master branch.
3. If there is a protection rule for the master branch, click the `Edit` button for that rule.
4. Enable the checkbox for the `Require status checks to pass before merging`.
5. If `Run unit tests` is a visible option for the `Status checks found in the last week for this repository`, enable that option.
6. If the `Run unit tests` option isn't displayed yet, it will display after a non-master branch has been pushed.
7. Create a branch with a test commit to confirm the above has enabled status checks for PRs in your repo.

A Continuous Deployment (CD) pipeline via GitHub Actions will likely land in this starter kit to complement the
CI workflow noted above.


## Prior Art

This repo is the successor of https://github.com/kamalgill/flask-appengine-template , now archived
due to legacy technology choices and the end-of-life of Python 2 on Jan 1 2020.
