from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib
matplotlib.pyplot.switch_backend('Agg')
# import io
# matplotlib.use("macOSX")
# matplotlib.get_backend()

def zcr_sigenergy(INPUTPATH, OUTPATH):
    try:
        [Fs, x] = audioBasicIO.read_audio_file(INPUTPATH)
        F_0, f_names_0 = ShortTermFeatures.feature_extraction(x[:,0], Fs, 0.050*Fs, 0.025*Fs)
        F_1, f_names_1 = ShortTermFeatures.feature_extraction(x[:,1], Fs, 0.050*Fs, 0.025*Fs)
        fig = plt.figure(figsize=(18, 8), dpi=200)
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        ax1.plot(F_0[0,:], label=f_names_0[0])
        ax1.plot(F_0[1,:], label=f_names_0[1])
        ax2.plot(F_1[0,:], label=f_names_1[0])
        ax2.plot(F_1[1,:], label=f_names_1[1])
        ax1.legend()
        ax2.legend()
        # Set common labels
        fig.text(0.5, 0.01, 'Frame no.', ha='center', va='center')
        fig.text(0.004, 0.5, 'Zero Crossing Rate / Signal Energy', ha='center', va='center', rotation='vertical')
        ax1.set_title('Channel 0')
        ax2.set_title('Channel 1')
        fig.tight_layout()

        # buf = io.BytesIO()
        # plt.savefig(buf, format='png')
        # plt.close()
        # plt_bytes = buf.getvalue()
        # buf.close()



        plt.savefig(OUTPATH + 'zcr_energy.png')
        plt.close()
        return "Complete"
    except Exception as e:
        return "Error: " + str(e)