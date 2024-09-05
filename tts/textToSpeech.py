from gtts import gTTS

def createTextToSpeech(text):
    tts = gTTS(text)
    tts.save('tts.mp3')
    pass