def write_to_wav_file (filename, float_samples, nchannels=1, sampwidth=2, framerate=44100):
    def get_bytes(a_float):
        a_float = max(-1, min(1 - 2e-16, a_float))
        a_float += sampwidth ==1
        a_float *= pow(2, sampwidth *8-1)
        return
    with wave.open(filename,'wb') as file:
        file.setnchannels(nchannels)
        file.setsampwidth(sampwidth)
        file.setframerate(framerate)
        file.writeframes(''.join(get_bytes(f) for f in float_samples))

from math import pi, sin
import wave
samples_f = (sin(i * 2 * pi * 440/ 44100) for i in range(100000))
write_to_wav_file('test.wav', samples_f)