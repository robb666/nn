# Imports the Google Cloud client library
# from google.cloud import speech
import os
from google.cloud import speech_v1 as speech


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = \
    r'C:\Users\PipBoy3000\Desktop\IT\projekty\nn\Speech To Text\text-to-speech-349604-9fb6a8e4da36.json'

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


# config = dict(language_code="en-US")
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    # sample_rate_hertz=16000,
    language_code="pl-PL",  # 'pl-PL'
)
# audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")
# audio = dict(uri="adres.wav")
audio = dict(uri="gs://tts1_magro/nrrej.wav")
speech_to_text(config, audio)














# import os
# # from oauth2client.service_account import ServiceAccountCredentials
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = \
#     r'C:\Users\PipBoy3000\Desktop\IT\projekty\nn\Speech To Text\
#       client_secret_886959131153-vmbtcc6jrj5gg0vhijqpotroh7atr918.apps.googleusercontent.com.json'
#
# # scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
# #          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
#
# "www.googleapis.com/speech.googleapis.com"
# # creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# # client = speech.SpeechClient.
#
#
#
#
#
#
# # Instantiates a client
# client = speech.SpeechClient()
#
# # The name of the audio file to transcribe
# gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
#
# audio = speech.RecognitionAudio(uri=gcs_uri)
#
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code="en-US",  # 'pl-PL'
# )
#
#
#
# # Detects speech in the audio file
# response = client.recognize(config=config, audio=audio)
#
# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))