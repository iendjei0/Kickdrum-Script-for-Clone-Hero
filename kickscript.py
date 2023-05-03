import pyaudio
import numpy as np
import keyboard
import time

# set up audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100,
                input=True, frames_per_buffer=4096)

# wait for 2 seconds before checking for sound
time.sleep(2)

# flag to indicate if 7 key has been pressed
key_pressed = False

# loop to continuously read audio data
while True:
    # read audio data and convert to numpy array
    data = np.frombuffer(stream.read(4096), dtype=np.int16)

    # calculate RMS amplitude of audio data
    rms = np.sqrt(np.mean(np.square(np.abs(data))))

    # check if RMS is above threshold to detect sound
    if rms > 50.0 and not key_pressed:
        # press the 7 key
        keyboard.press("5")
        print(rms)
        keyboard.release("5")
        key_pressed = True
        # time.sleep(0.001)  # add 100ms leeway to the timing
    elif rms <= 50.0 and key_pressed:
        key_pressed = False
