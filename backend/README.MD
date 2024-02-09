# Initialization

Create a python virtual environment with
```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
```


# To run

## Linux
First check that you have the virtual environment active
```bash
source .venv/bin/activate
```
## Windows
```bash
source .venv/Scripts/activate
```

Then run
## Linux
```bash
flask --app app run --debug
```
## Windows
```bash
python3 -m flask --app app run --debug --host=0.0.0.0
```
