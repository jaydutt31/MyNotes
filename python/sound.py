import pyttsx3
from playsound import playsound



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',5.0)    # setting up volume level  between 0 and 1


rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate


engine.say("maggi bana do ")
engine.runAndWait()



#Changing Voices

