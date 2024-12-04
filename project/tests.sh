#!/bin/bash

# Run pipeline.sh first, since pipeline.sh downloads three data sets
bash ./pipeline.sh

# Run the Python tests
python ./tests.py