import os
from google.cloud import speech_v1 as speech
from constants import PATH_HOME, PATH_OFFICE
import pyaudio
import wave


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH_HOME if os.path.exists(PATH_HOME) else PATH_OFFICE


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()


"""Upload to GS"""
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

upload_blob('tts1_magro', './output.wav', 'nrrej_desktop')


"speech to text"
def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 60)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")


config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="pl-PL",
    # sample_rate_hertz=16000,
)

# audio_set = ['adres', 'pesel', 'nrrej']
# audio_set = ['adres']
audio_set = ['nrrej_desktop']
for wav in audio_set:
    audio = dict(uri=f"gs://tts1_magro/{wav}")
    speech_to_text(config, audio)


"""pyscript"""
# https://console.cloud.google.com/welcome?project=text-to-speech-349604