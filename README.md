## Starter Kit for Flask on Google App Engine

Starter project template for running a Flask-based application on
Google App Engine Standard Python 3 Runtime.

The application structure of this starter kit is loosely inspired by Miguel Grinberg's 
[Flask Web Development (Second Edition)](http://oreilly.com/catalog/0636920089056) book,
with the book's companion repo at https://github.com/miguelgrinberg/flasky


### Development Setup Requirements

- Python 3.7 or later
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
- Windows, MacOS, and Linux development environments are supported


## Development Setup Instructions

Assuming the development setup requirements above have been satisfied,
run the following in a terminal (git-bash is recommended on Windows) after cloning the repo
to set up your local development environment.

```bash 
# Install local dev requirements
pip install -r requirements-dev.txt
```


## Running the Development Server

Issue the following command to run the development server...

```bash
# Cross-platform -- works on Windows, MacOS and Linux, albeit without a --reload option
waitress-serve app:application
```

If you're on Linux or MacOS you can run the app via gunicorn, which offers a `--reload` option and
more closely emulates the App Engine production runtime, which uses gunicorn by default.

```bash
# Linux and MacOS only, use --reload flag to automatically reload on code changes
gunicorn app:application --reload
```

The app is viewable at http://localhost:8080 -- sample hello endpoint is at http://localhost:8080/api/v1/hello/world


### Customizing the HTTP Port

The app runs on port 8080 by default.  

To customize the port, pass the `--port` option as in the following example...

```bash
# Set port to 9000
waitress-serve --port=9000 app:application
```
