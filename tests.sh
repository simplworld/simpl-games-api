#!/bin/bash

pip install -r requirements.txt

PYTHONPATH=. py.test
