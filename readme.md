# Testing whisper ai
This repo is just to test whisper ai and trying to make it real time.

## Get started
Install the pip packages with

```
pip install -r requirements.txt
```
Get the vosk model with:

On linux:
```
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 model
```

On windows:
```
Invoke-WebRequest -Uri "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip" -OutFile "vosk-model-small-en-us-0.15.zip"

Expand-Archive -Path "vosk-model-small-en-us-0.15.zip" -DestinationPath ".\model"

Rename-Item -Path ".\vosk-model-small-en-us-0.15" -NewName "model"
```
