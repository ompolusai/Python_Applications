import os,time
from gtts import gTTS
mytext = 'hello ompolu!'
language = 'en'
time.sleep(9)
mytext1 = 'welcome to srkr!'
time.sleep(9)
mytext2 = 'welcome to ece!'
myobj = gTTS(text=mytext+mytext1+mytext2, lang=language, slow=False)
myobj.save("welcome.mp3")
os.startfile("welcome.mp3")