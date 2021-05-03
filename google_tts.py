# https://gtts.readthedocs.io/en/latest/module.html#examples

# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from gtts import gTTS
import os



# define variables
s = "escape with plane"
file = "file.mp3"

# initialize tts, create mp3 and play
tts = gTTS(s, lang='en')
tts.save(file)
os.system("mpg123 " + file)#play mp3
