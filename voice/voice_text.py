import warnings
import whisper
import os

import whisper

def transcribe_audio(audio_path: str, fp16: bool = False) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, fp16=fp16)
    print(result)
    return result["text"]
