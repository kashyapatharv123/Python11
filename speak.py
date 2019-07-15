from gtts import gTTS
from playsound import playsound
tts = gTTS('Hello how r u I am fine thank you')
tts.save('abc.mp3')
playsound('abc.mp3')