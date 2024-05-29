#!/usr/bin/env bash

# activate
source ./env/bin/activate

# run the code
python src/main.py "$@"

# close
deactivate