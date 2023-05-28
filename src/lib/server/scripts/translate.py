import os
import sys
import openai
import pysrt


openai.api_key = os.getenv("OPENAI_API_KEY")
text_input = sys.stdin.read()
srt = pysrt.from_string(text_input)

base_prompt = (
    "You are going to be an English to Korean translator."
    "I will give you a transcript from a video talking about the difference"
    "different levels of software engineers."
    "Please translate the following into polite Korean starting from"
    "[START] until [END]:\n[START]\n"
)


def translate(text):
    prompt = base_prompt + text + "\n[END]"
#
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        temperature=0
    )

    raw_translation = res.choices[0].text
    stripped_start = raw_translation.replace('[START]', '').strip()
    translation = stripped_start.replace('[END]', '').strip()
    return translation


for index, subtitle in enumerate(srt):
    subtitle.text = translate(subtitle.text)
    print(subtitle, flush=True)
