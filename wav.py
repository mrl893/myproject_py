from simpleaudio import play_buffer
import wave
import simpleaudio.functionchecks as fc

# fc.run_all()
fc.LeftRightCheck.run()
with wave.open('test.wav', 'rb') as file:
    p = file.getparams()
    frames = file.readframes(-1)
    play_buffer(frames, p.nchannels, p.sampwidth, p.framerate)
