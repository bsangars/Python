from gtts import gTTS
import os

text = "Welcome to the Text to speech conversion using python"
language = 'en'
speech = gTTS(text=text, lang = language, slow=False)
speech.save("text.mp3")
os.system("start text.mp3")