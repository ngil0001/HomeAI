import os
import struct
import sys
import wave
from dotenv import load_dotenv
import pvporcupine
import pyaudio
from process import process_text
from voice_text import transcribe_audio
from actions import categorize


def record_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 if sys.platform == 'darwin' else 2
    RATE = 44100
    RECORD_SECONDS = 5

    with wave.open('voice/output.wav', 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))
        print('Done')
        stream.close()
        p.terminate()
    
    transcribed_text = transcribe_audio('voice/output.wav')
    entities = process_text(transcribed_text)
    categorize(entities)

#---------------------------pvporcupine------section---------------------------------------------
# Load environment variables
load_dotenv()

# Get the access key from the environment variable
access_key = os.getenv('PICOVOICE_API_KEY')

# Initialize Porcupine with the access key and the wake word 'jarvis'
handle = pvporcupine.create(access_key=access_key, keywords=['jarvis'])

# Set up PyAudio parameters
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=handle.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=handle.frame_length)

# Replace print with a visual indicator
print('Listening for wake word...')
try:
    while True:
        # Read a chunk of audio data from the input stream
        pcm = audio_stream.read(handle.frame_length, exception_on_overflow=False)
        
        # Convert byte data to int16
        pcm = struct.unpack_from("h" * handle.frame_length, pcm)

        # Pass the audio frame to Porcupine's process method
        keyword_index = handle.process(pcm)
        if keyword_index >= 0:
            #replace print with a visual indicator/sound
            print('Keyword detected!')
            # Run transcription and process commands
            record_audio()
            break
except KeyboardInterrupt:
    print('Exiting...')
finally:
    # Clean up resources
    audio_stream.close()
    pa.terminate()
    handle.delete()
