import sys
import os
import speech_recognition as sr
import ffmpeg
import pydub
from pydub import AudioSegment
r = sr.Recognizer()
audio_fullpath=sys.argv[1]
audio_name=sys.argv[2]
audio_formats=["mp3",".mp4a","wav","flac","3gp","webm"]
if audio_fullpath.endswith(tuple(audio_formats)):
    def conversion(path):
        if path.endswith(tuple('.mp3')):
            sound= AudioSegment.from_mp3(path)
            path=path.replace(".mp3",".wav")
            sound.export(path,format='wav')
        if path.endswith(tuple('.mp4a')):
            sound= AudioSegment.from_file(path)
            path=path.replace(".mp4a",".wav")
            sound.export(path,format='wav')
        if(path.endswith(tuple('.wav'))):
            return path
        if(path.endswith(tuple('.flac'))):
            sound= AudioSegment.from_file(path)
            path=path.replace(".flac",".wav")
            sound.export(path,format='wav')
        if path.endswith(tuple('.3gp')):
            sound= AudioSegment.from_file(path)
            path=path.replace(".3gp",".wav")
            sound.export(path,format='wav')
        if path.endswith(tuple('.webm')):
            sound= AudioSegment.from_file(path)
            path=path.replace(".webm",".wav")
            sound.export(path,format='wav')
        return path
    # open the file
    def aud(path):
        with sr.AudioFile(path) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            return text
    path=conversion(audio_fullpath)
    output=aud(path)
    print(output)

else:
    print("Please choose only specified path")
 

    




