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
    sf.write("res-f2.wav",audio,fs)

    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)

    # Wait for playback to finish before exiting
    play_obj.wait_done()


signal2, fs2 = sf.read('voice2.wav')
signal2 = signal2[:]
# Compute fft
f2 = np.fft.fft(signal2)
# Convert to polar (magnitude and phase)
m2 = np.abs(f2)
p2 = np.angle(f2)



signal, fs = sf.read('voice.wav')
tmp = signal[:len(signal2)]
signal=tmp
# Compute fft
f = np.fft.fft(signal)
# Convert to polar (magnitude and phase)
m = np.abs(f)
p = np.angle(f)




p_tmp=p2
p2=p
p=p_tmp

m_tmp=m
m=m2
m2=m_tmp

#play_audio(m, p, fs)
play_audio(m2, p2, fs2)