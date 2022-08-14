# Voice Recorder using Python
import sounddevice
from scipy.io.wavfile import write


def voice_recorder(sounds,file):
    print("recording started...")
    recording = sounddevice.rec((sounds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print('recording finished')
voice_recorder(10,'record.wav')


