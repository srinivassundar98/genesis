'''import os
import time
import speech_recognition as sr
from gtts import gTTS
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
from oral_viva import oral_viva


oral_viva_q = ["What is a constructor", "list types of constructors"]
oral_viva_key=["member function initialises objects called automatically object created",
               "three types parameterized default copy"]
quest=[oral_viva(oral_viva_q[0],word_tokenize(oral_viva_key[0])),
       oral_viva(oral_viva_q[1],word_tokenize(oral_viva_key[1]))
       ]
oviva = 0


for oral_viva in quest:
    text = oral_viva.prompt
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("oral.mp3")
    os.system("oral.mp3")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        time.sleep(10)
        print("Speak Anything :")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        ch=input("is this correct Y/N")
        if ch =='Y':
            ans = word_tokenize(text)
            if ans == oral_viva.answer:
                oviva+=1
                print("correct!")
            else:
                print("wrong")
        else:
            break
print("score:"+str(oviva))'''













