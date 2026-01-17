# TagaTranscribe
 ---
Hello! My name is Brad Urbiztondo. This is for my 2026 Stem Fair Project.

Tagalog is spoken by more than 28 million people in the Philippines and over 4 million Filipino Americans, yet it remains a low‑resource language in speech recognition.
My investigation examines the effect of finetuning Whisper-small on Tagalog and Taglish audio recorded from Filipino American speakers. Audio files were gathered from willing participants in my school’s (Kasama) Filipino Cultural Club. I will test if this does improve transcription accuracy by recording and comparing the (WER) Word Error Rate before & after.
Existing datasets rarely include American‑accented Tagalog, mixed English‑Tagalog speech, imperfect speech, or natural conversational patterns. Improving transcription quality has real community impact because more accurate ASR leads directly to better translation, accessibility, education, and communication tools for millions of Tagalog speakers worldwide, including over 4 million Filipino Americans in the United States (Pew Research Center, 2023) 
---
Here is the link to my model uploaded on Hugging Face
https://huggingface.co/BradUrbiz/tagatranscribe-v1
---
Audio recordings are anonymzed and feel free to use the model
---
I collected around 700 audio files of speech. This was split up into about 80% train, 10% validation, and 10% test sets. OpenAI's Whisper-small was finetuned on my data.
Total epochs: 10
Batch size: 2
Gradient accumulation: 8
Effective batch size: 16
Learning rate: 1e-05


<img width="328" height="377" alt="Screenshot 2026-01-16 194810" src="https://github.com/user-attachments/assets/ab86f1c6-6330-4fd5-87fb-13978743c26d" />
---
For full explanation, check out Youtube video (not made yet)

