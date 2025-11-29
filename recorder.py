import pyaudio
import wave
import os
import audioop
import threading
import keyboard

format = pyaudio.paInt16
channel = 1
rate = 16000
chunk = 1024
silence = 1.0
noise_needed = 100

pyaudio = pyaudio.PyAudio()

os.makedirs("audio", exist_ok=True)

files = [file for file in os.listdir("audio") if file.endswith(".wav")]
if files:
    files.sort()
    file_index = int(files[-1].split(".")[0]) + 1
else:
    file_index = 1

stream = pyaudio.open(
    format=format,
    channels=channel,
    rate=rate,
    input=True,
    frames_per_buffer=chunk
)

frames = []
active = False
silence_counter = 0
is_paused = False

def pause():
    global is_paused
    is_paused = not is_paused
    print("Paused" if is_paused else "Resumed")

def paused():
    return is_paused

def listen_for_pause():
    while True:
        keyboard.wait('p')
        pause()

threading.Thread(target=listen_for_pause, daemon=True).start()

while True:
    if paused():
        continue

    data = stream.read(chunk)
    loud = audioop.rms(data, 2)

    if loud > noise_needed:
        if not active:
            active = True
            frames = []
        frames.append(data)
        silence_counter = 0
    else:
        if active:
            frames.append(data)
            silence_counter += chunk / rate
            if silence_counter > silence:
                active = False
                filename = f"audio/{file_index:04d}.wav"
                wavefile = wave.open(filename, "wb")
                wavefile.setnchannels(channel)
                wavefile.setsampwidth(pyaudio.get_sample_size(format))
                wavefile.setframerate(rate)
                wavefile.writeframes(b"".join(frames))
                wavefile.close()
                print(f"Saved {filename}")
                file_index += 1