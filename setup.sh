#!/bin/bash

pip install virtualenv

virtualenv env

source env/bin/activate

pip install -r requirements.txt

echo -e "\n\nApplication Starts:\n"

python main.py
