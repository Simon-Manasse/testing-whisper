from faster_whisper import WhisperModel
import torch

def transcribeFile():
    """
    Transcribes the audio file 'output.wav' and saves the transcription to 'prompt.txt'.

    This function initializes a Whisper model to perform transcription using GPU with FP16 precision.
    It processes the audio file and generates a text transcription based on the audio content.

    The function performs the following steps:
    1. Initializes the Whisper model with the specified size and device settings.
    2. Transcribes the audio file and retrieves both the transcription segments and metadata.
    3. Prints the detected language and its probability.
    4. Concatenates the text from all transcription segments into a single string.
    5. Prints the full transcribed text.
    6. Saves the transcribed text to 'prompt.txt'.

    Returns:
        None
    """
    model_size = "large-v3"  # Choose the model size ('tiny', 'base', 'small', 'medium', 'large')

    # Initialize the Whisper model to run on GPU with FP16 precision
    model = WhisperModel(model_size, device="cuda",device_index=0, compute_type="float16")

    # Transcribe the audio file and get segments and metadata
    segments, info = model.transcribe("./output.wav", beam_size=5)

    # Print detected language and its probability
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    # Initialize a variable to accumulate the transcribed text
    transcribedText = ""

    # Concatenate text from each segment
    for segment in segments:
        transcribedText += segment.text

    # Print the full transcribed text
    print(transcribedText)

    # Save the transcribed text to a file
    with open('prompt.txt', 'w') as f:
        f.write(transcribedText)
    
    del model
    torch.cuda.empty_cache()
    pass
