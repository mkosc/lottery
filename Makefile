VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make test"
	@echo "       run tests"
	@echo "make lint"
	@echo "       run pylint and mypy"
	@echo "make run"
	@echo "       run project"
	@echo "make clean"
	@echo "       clean created venv"

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate:
	python3 -m venv $(VENV_NAME)
	${PYTHON} -m pip install -Ur requirements.txt

test: venv
	${PYTHON} -m pytest

lint: venv
	${PYTHON} -m pylint src tests
	${PYTHON} -m mypy src tests

run: venv
	${PYTHON} run.py ${PARAMS}

# TODO: cleaning .pyc files, mypy and pytest cache
clean:
	rm -rf venv
