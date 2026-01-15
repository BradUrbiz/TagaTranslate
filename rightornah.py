# dont forgot to install ffmpeg and openai-whisper

import whisper

model = whisper.load_model("small")

audio_path = "audio/0157.wav" 
result = model.transcribe(audio_path)

print(result["text"])
