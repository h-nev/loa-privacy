#!/bin/bash

cd ..

python3 -m venv loa-privacy

cd loa-privacy

source bin/activate && pip install -r requirements.txt