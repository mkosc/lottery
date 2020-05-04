# Lottery

A simple lottery application

Usage:

to run application invoke:
    make run PARAMS='${PARAMS}'
    
Example:
    
    make run PARAMS='-d participants2'
    
Available makefile targets:
- venv - creates virtual environment
- test - runs unit tests
- lint - runs mypy and pylint
- run - run app
- clean - cleans virtual environment

Available parameters:

  -d, --data [required]
  
  -ft, --file-type

  -t, --template
  
  -o, --output
  
  invoke with --help for details.
