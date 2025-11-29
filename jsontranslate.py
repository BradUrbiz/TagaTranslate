import json
import whisper
import os

dataset = "tagalog_to_english.jsonl"
model_type = "large"

model = whisper.load_model(model_type)

with open(dataset, "r", encoding="utf-8") as f:
    items = [json.loads(line) for line in f]

for item in items:
    if not item.get("text", "").strip() and os.path.exists(item["audio"]):
        res = model.transcribe(item["audio"], task="translate", language="tl")
        item["text"] = res["text"].strip()

with open(dataset, "w", encoding="utf-8") as f:
    for item in items:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print("Done")