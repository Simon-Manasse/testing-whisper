import wave
import sys
import pyaudio
from faster_whisper import WhisperModel
import torch
import pyttsx3
import tts.textToSpeech as tts
import audio.recording as recording  # Import recording module
import transcribe.transcribeToText as transcribe  # Import transcribe module
import transcribe.readTranscribedText as readInPrompt  # Import readInPrompt module
import aiModel.postToModel as aiModel  # Import aiModel module


recording.recordAudio()

# Transcribe the recorded audio file to text
transcribe.transcribeFile()

# Read the transcribed text from 'prompt.txt'
prompt = readInPrompt.readInPrompt()



# Send the transcribed text to the AI model with a specific prompt ID
aiResponse= aiModel.sendPrompt("gemma2:2b", "gimme a recipie for apple pie")
# Creating a an mp3 file to play
tts.createTextToSpeech(aiResponse)
torch.cuda.empty_cache()

