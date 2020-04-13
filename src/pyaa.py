from src.pyAudioAnalysis.pyAudioAnalysis import audioBasicIO
from src.pyAudioAnalysis.pyAudioAnalysis import ShortTermFeatures
import matplotlib.pyplot as plt

def runall():
    [Fs, x] = audioBasicIO.read_audio_file("/Users/rehanguha/Work/Personal/AudioAnalytica/input/a.wav")

    F, f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.050*Fs, 0.025*Fs)
    plt.subplot(2,1,1) 
    plt.plot(F[0,:])
    plt.xlabel('Frame no') 
    plt.ylabel(f_names[0])
    plt.subplot(2,1,2); plt.plot(F[1,:])
    plt.xlabel('Frame no')
    plt.ylabel(f_names[1])
    plt.savefig("temp")