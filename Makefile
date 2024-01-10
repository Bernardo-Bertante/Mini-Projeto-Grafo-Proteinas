VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: src/requirements.txt
		python3 -m venv $(VENV)
		$(PIP) install -r src/requirements.txt

run: $(VENV)/bin/activate
		$(PYTHON) src/main.py 

clean:
		rm -rf _pycache_
		rm -rf $(VENV)