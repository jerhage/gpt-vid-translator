import os
import sys
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
video_id = sys.argv[1]
# file_path = os.path.join(os.getcwd())
print('Your current dir is: ' + os.getcwd())

print(f'Your video_id is {video_id}')
