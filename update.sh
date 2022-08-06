#!/bin/bash

script=$(realpath "$0")
scriptpath=$(dirname "$script")

python3 $scriptpath/update_db.py

