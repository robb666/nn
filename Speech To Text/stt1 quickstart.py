
import os
from google.cloud import speech_v1 as speech
from constants import PATH_HOME, PATH_OFFICE


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = PATH_HOME if os.path.exists(PATH_HOME) else PATH_OFFICE


def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")



config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="pl-PL",
    # sample_rate_hertz=16000,
)

audio_set = ['adres', 'pesel', 'nrrej']
for wav in audio_set:
    audio = dict(uri=f"gs://tts1_magro/{wav}.wav")
    speech_to_text(config, audio)


