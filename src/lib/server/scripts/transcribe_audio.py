import os
import sys
import openai

# TODO: allow for custom prompt?

openai.api_key = os.getenv("OPENAI_API_KEY")
video_id = sys.argv[1]
path_to_audio = os.path.join('../tmp/', video_id + '.webm')
audio = open(path_to_audio, "rb")

transcript = openai.Audio.transcribe(
    file=audio,
    model='whisper-1',
    response_format='srt',
    prompt=(
        'I am a software engineer who talking about programming concepts.'
    )
)

print(transcript)
