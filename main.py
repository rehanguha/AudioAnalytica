#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:58:29 2020

@author: rehanguha
"""

from flask import Flask, request, json
import speech_recognition as sr
from os import path
from wit import Wit
import src.audioanalysis as aa
import src.wavefile as wave
from IPython import embed
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)



WIT_AI_KEY = "SFAWDUXBNSBXQNWXI5EMQ74RJINBLTWF"  # Wit.ai keys are 32-character uppercase alphanumeric strings
client = Wit(WIT_AI_KEY)


# /transcribe?filename=input/b.wav
@app.route("/transcribe", methods = ['GET', 'POST'])
def transcribe():
    filename = request.args.get('filename')
    
    r = sr.Recognizer()
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), filename)
    
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file
    
#    # recognize speech using Sphinx
#    try:
#        return r.recognize_sphinx(audio)
#    except sr.UnknownValueError:
#        return "Sphinx could not understand audio"
#    except sr.RequestError as e:
#        return "Sphinx error; {0}".format(e)
    
    with open(AUDIO_FILE, 'rb') as f:
        resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
    return(str(resp))    
    
    
#    try:
#        return(r.recognize_wit(audio, key=WIT_AI_KEY))
#    except sr.UnknownValueError:
#        return("Wit.ai could not understand audio")
#    except sr.RequestError as e:
#        return("Could not request results from Wit.ai service; {0}".format(e))
    
# /quantileanalysis?filename=<inputfilename>&path=<inputpath>
@app.route("/quantileanalysis", methods = ['GET', 'POST'])
def quantileanalysis():
    filename = request.args.get('filename')
    path = request.args.get('path')
    data = aa.mysptotal(path, filename, "src/myspsolution.praat")
    return data

# /waveform?filename=<inputfilename>
@app.route("/waveform", methods = ['GET', 'POST'])
def waveform():
    filename = request.args.get('filename')
    outputpath = "output/"
    status = wave.audio_waveplot(INPUTPATH=filename,OUTPATH=outputpath)
    return status


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=5001)