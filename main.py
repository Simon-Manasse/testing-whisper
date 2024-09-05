import wave
import sys
import pyaudio
from faster_whisper import WhisperModel
import torch
import audio.recording as recording
import transcribe.transcribeToText as transcribe
import transcribe.readTranscribedText as readInPrompt
import aiModel.postToModel as aiModel
recording.recordAudio()

transcribe.transcribeFile()

prompt= readInPrompt.readInPrompt()

torch.cuda.empty_cache()
aiModel.sendPrompt("gemma2:2b",prompt)



