# Data Mining Experiment

## What?

A demonstration Python data project showing:

* The cookiecutter project layout <https://github.com/drivendata/cookiecutter-data-science>,
* a packaged API wrapper <https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python>, 
* some tests <https://docs.pytest.org/en/latest/getting-started.html> and 
* a unicode sandwich <http://johnbachman.net/building-a-python-23-compatible-unicode-sandwich.html>

## How to get set up?

Use a virtual environment, so...

    pip install virtualenv
    pip install virtualenvwrapper-win

or if you are not on Windows

    sudo apt install virtualenv
    sudo apt install virtualenvwrapper

Create a virtual enviroment for the project

    mkvirtualenv yearlet

Install the supporting packages

    pip install -r requirements.txt

Run the tests (the pytests don't run in Visual Studio which is a shame)

    pytest

When you are done deactivate the virtual environment with

    deactivate

## Project Structure

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── src                <- Unit tests for the package.
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```
