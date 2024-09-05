import wave
import sys
import pyaudio

def recordAudio():
    """
    Records audio from the default input device and saves it to 'output.wav'.

    The function configures audio recording parameters such as chunk size, format,
    number of channels, sample rate, and recording duration. It initializes 
    a PyAudio stream, captures audio data in chunks, and writes it to a WAV file.

    The number of audio channels is set to mono (1) for macOS and stereo (2) otherwise.
    The audio is recorded for a duration of 5 seconds at a sample rate of 44,100 Hz 
    with a chunk size of 1,024 frames.

    The function performs the following steps:
    1. Opens a new WAV file for writing audio data.
    2. Configures audio parameters and initializes the PyAudio stream.
    3. Records audio in chunks and writes it to the WAV file.
    4. Closes the audio stream and terminates the PyAudio instance.
    """
    
    # Define constants for audio recording
    CHUNK = 1024  # Number of audio frames per buffer
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    # Number of audio channels: mono (1) for macOS, stereo (2) otherwise
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100  # Sampling rate (samples per second)
    RECORD_SECONDS = 5  # Duration of the recording in seconds

    # Open a new wave file to write audio data
    with wave.open('output.wav', 'wb') as wf:
        # Initialize the PyAudio object
        p = pyaudio.PyAudio()
        
        # Set up the wave file with the specified audio parameters
        wf.setnchannels(CHANNELS)  # Number of audio channels
        wf.setsampwidth(p.get_sample_size(FORMAT))  # Sample width (bytes per sample)
        wf.setframerate(RATE)  # Frame rate (samples per second)

        # Open an audio stream for recording
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        # Read data from the stream in chunks and write to the wave file
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))  # Read and write audio data in chunks
        
        print('Done')

        # Close the stream and terminate PyAudio
        stream.close()
        p.terminate()

    # End of the function
    pass
