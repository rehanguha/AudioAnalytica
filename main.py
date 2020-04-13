#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:58:29 2020

@author: rehanguha
"""
from src.utils import extractFilename, mkDIR
from flask import Flask, request, json
import speech_recognition as sr
from os import path
from wit import Wit
import src.audioanalysis as aa
import src.wavefile as wave
from IPython import embed
from flask_cors import CORS
from src.CONSTANTS import *

app = Flask(__name__)
cors = CORS(app)

client = Wit(WIT_AI_KEY)

# /transcribe?filename=<inputfilename with path>
@app.route("/transcribe", methods = ['GET', 'POST'])
def transcribe():
    AUDIO_FILE = request.args.get('filename')
    
    with open(AUDIO_FILE, 'rb') as f:
        resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
    
    return(str(resp))    


# /quantileanalysis?filename=<inputfilename>&path=<inputpath>
@app.route("/quantileanalysis", methods = ['GET', 'POST'])
def quantileanalysis():
    filename = request.args.get('filename')
    data = aa.mysptotal(filename, PRAAT_FILE)
    return data

# /waveform?filename=<inputfilename with path>
@app.route("/waveform", methods = ['GET', 'POST'])
def waveform():
    filename = request.args.get('filename')
    name = extractFilename(filename)
    outputpath = "output/" + str(name) + "/"
    mkDIR(outputpath)
    status = wave.audio_waveplot(INPUTPATH=filename,OUTPATH=outputpath)
    return status

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=5001)