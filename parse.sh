#!/bin/sh

echo "Parse organizations"
python3 manage.py parse_organizations

echo "Parse operators"
python3 manage.py parse_operators

echo "Parse weapons"
python3 manage.py parse_weapons