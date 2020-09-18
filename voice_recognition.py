import speech_recognition as sr
from drawchar import *

#####################################################################
# Voice recognition
#####################################################################

r = sr.Recognizer()

text = ''
with sr.Microphone() as source:
    print('Say Something...: ')
    audio = r.listen(source)
    lang = 'en-Us'
    #lang = 'es-Es'
    
    try:
        text = r.recognize_google(audio, language=lang)
        print(text)
        
    except:
        print('I am sorry! I can not understand!')
draw(text.lower())