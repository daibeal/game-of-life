# Path: Makefile

# Define variables for convenience
PYTHON = python3
PYTEST = pytest
PYLINT = pylint
SRC = src

# Define a default target that will run all tests and checks
all: install lint run

# Define a target to run pylint
lint: 
	$(PYLINT) $(SRC)/*.py

# Define a target to install the requirements
install: 
	$(PYTHON) -m pip install -r requirements.txt

# Define a target to run the program
run: 
	$(PYTHON) $(SRC)/app.py