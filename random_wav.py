from random import random
add_noise = lambda value: value + (range() - 0.5) * 0.03
samples_f = (add_noise(f) for f in  read_wav_file('test.wav'))
write_to_wav_file('test.wav', samples_f)
