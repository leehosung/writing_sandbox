#!/bin/bash
if [[ $TRAVIS_BRANCH == 'master' && $TRAVIS_PULL_REQUEST == 'false' ]]; then
  echo "test all"
  python3 manage.py test 
else
  echo "test only unittest"
  python3 manage.py test quiz
fi
