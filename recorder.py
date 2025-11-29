import pyaudio
import wave
import os
import audioop

format = pyaudio.paInt16
channel = 1
rate = 16000
chunk = 1024
silence = 1.0
noise_needed = 100

pyaudio = pyaudio.PyAudio()

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

while True:
    data = stream.read(chunk)
    loud = audioop.rms(data, 2)

    if loud > noise_needed:
        if not active:
            print("Start")
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