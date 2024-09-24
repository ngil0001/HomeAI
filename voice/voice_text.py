import warnings
import whisper
import os

import whisper

model = whisper.load_model("base")
result = model.transcribe("voice\output.wav", fp16=False)
print(result["text"])