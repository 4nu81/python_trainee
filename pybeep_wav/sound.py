import numpy as N
import wave

class SoundFile:
    def init(self, signal):
        self.file = wave.open('test.wav', 'wb')
        self.signal = signal
        self.sr = 44100

    def write(self):
        self.file.setparams((1, 2, self.sr, 44100*4, 'NONE', 'noncompressed'))
        self.file.writeframes(self.signal)
        self.file.close()

    def prep_signal(self, frequency, duration):
        # let's prepare signal
        #duration = 1 # seconds
        samplerate = 44100 # Hz
        samples = duration*samplerate
        period = samplerate / float(frequency) # in sample points
        omega = N.pi * 2 / period

        xaxis = N.arange(int(period),dtype = N.float) * omega
        ydata = 16384 * N.sin(xaxis)

        signal = N.resize(ydata, (samples,))

        ssignal = ''
        for i in range(len(signal)):
           ssignal += wave.struct.pack('h',signal[i]) # transform to binary
        return ssignal

    def __init__(self, lst):

        ssignal = ''
        for freq, dur in lst:
            ssignal += self.prep_signal(freq, dur)

        self.init(ssignal)
        self.write()
        print 'file written'
