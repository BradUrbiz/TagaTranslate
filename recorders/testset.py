import sounddevice as sd
import soundfile as sf
import numpy as np
import os
import sys
import select

RATE = 16000
CHANNELS = 1

# Always use the real testset folder, no matter where the script is run
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TESTSET_DIR = os.path.join(BASE_DIR, "testset")

# Make sure the folder exists (but never creates testset/testset)
os.makedirs(TESTSET_DIR, exist_ok=True)

# Find the latest file number
files = [f for f in os.listdir(TESTSET_DIR) if f.endswith(".wav")]
if files:
    files.sort()
    file_index = int(files[-1].split(".")[0]) + 1
else:
    file_index = 1

print("Enter = start")
print("Enter = stop")
print("ctrl+c = quit")

while True:
    input(f"Enter = start recording {file_index:04d}.wav...")

    print("ON, Enter = stop.")
    frames = []

    with sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype='int16') as stream:
        while True:
            data, _ = stream.read(1024)
            frames.append(data)

            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                input()
                break

    audio = np.concatenate(frames, axis=0)

    # Save into the correct testset folder
    filename = os.path.join(TESTSET_DIR, f"{file_index:04d}.wav")
    sf.write(filename, audio, RATE)
    print(f"saved {filename}\n")

    file_index += 1
