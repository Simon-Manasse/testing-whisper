import wave
import sys
import pyaudio
from faster_whisper import WhisperModel
import torch
import audio.recording as recording  # Import recording module
import transcribe.transcribeToText as transcribe  # Import transcribe module
import transcribe.readTranscribedText as readInPrompt  # Import readInPrompt module
import aiModel.postToModel as aiModel  # Import aiModel module

# Record audio and save it to 'output.wav'
recording.recordAudio()

# Transcribe the recorded audio file to text
transcribe.transcribeFile()

# Read the transcribed text from 'prompt.txt'
prompt = readInPrompt.readInPrompt()

# Clear the CUDA memory cache
torch.cuda.empty_cache()

# Send the transcribed text to the AI model with a specific prompt ID
aiModel.sendPrompt("gemma2:2b", prompt)
