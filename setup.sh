#!/bin/bash

# Creating virtual environment for python to negate problems
python -m venv .venv
# Activating virtual environment
source .venv/bin/activate
# Installing needed packages
pip install -r requirements.txt

# Downloading vosk model
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 model