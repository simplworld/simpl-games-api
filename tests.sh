#!/bin/bash

pip install -r requirements/test.txt

PYTHONPATH=. py.test
