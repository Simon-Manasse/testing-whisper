from faster_whisper import WhisperModel

def transcribeFile():
    model_size = "tiny"

    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    segments, info = model.transcribe("./output.wav", beam_size=5)

    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    transcribedText=""

    for segment in segments:
        transcribedText+=segment.text

    print(transcribedText)
    with open('prompt.txt', 'w') as f:
        f.write(transcribedText)
    pass