#!/bin/bash
export SAUCE="TRUE"
export SAUCE_SERVER_URL="http://writing-sandbox.herokuapp.com"
python3 manage.py test functional_tests
