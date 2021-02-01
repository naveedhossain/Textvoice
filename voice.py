from gtts import gTTS

import os

f = open('voice.txt')
x = f.read()

language = "en"

audio = gTTS(text=x,lang=language,slow=False)

audio.save("voice.wav")
os.system("voice.txt")
