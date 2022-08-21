import numpy as np
import soundfile as sf
import simpleaudio as sa


def play_audio(m, p, fs):
    # Combine magnitude and phase parts
    f = m * np.exp(1j * p)

    # Computer inverse fft
    y = np.fft.ifft(f)
    y = np.real(y)

    # Convert to 16-bit data
    audio = y * (2 ** 15 - 1)
    audio = audio.astype(np.int16)
    sf.write("res-c1.wav",audio,fs)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()



signal, fs = sf.read('mic.wav')
# Compute fft
f = np.fft.fft(signal)
# Convert to polar (magnitude and phase)
m = np.abs(f)
p = np.angle(f)





##//////////c1
#for i in range(0,len(p)):
#    p[i]+=i*(np.pi/2)
#

#//////////c2
#for i in range(0,len(p)):
#    p[i]+=i*(np.pi/2)*-1


##//////////c3
#for i in range(0,len(p)):
#    p[i]+=i*(np.pi)


play_audio(m, p, fs)