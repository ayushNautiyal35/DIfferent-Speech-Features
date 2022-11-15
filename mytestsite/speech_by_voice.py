import speech_recognition as sr
r = sr.Recognizer()

    # read the audio data from the default microphone
audio_data = r.record(sr.Microphone(), duration=10)
    # convert speech to text
text = r.recognize_google(audio_data)
output=text
print(output)