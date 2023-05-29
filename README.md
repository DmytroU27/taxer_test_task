### Installing Dependencies
1. Python 3.9 - Follow instructions to install the latest version of python for your platform in the python docs

2. Virtual Enviornment - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

3. PIP Dependencies - Once you have your virtual environment setup and running, install dependencies by naviging to the project directory and running:

```bash
# On Windows:
python -m venv venv

venv/Scripts/activate.bat

pip install -r requirements.txt

## Change your path for 'test_data' folder in configuration.py (TEST_DATA_FOLDER_PATH variable)
### Path must be closed with symbol '/'
pytest -s -v  tests/test_base_page.py
```
