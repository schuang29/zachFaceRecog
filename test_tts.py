import pyttsx3

# initialize Text-to-speech engine
engine = pyttsx3.init()

# speed up the voice a little
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+25)

# make it a little louder
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.25)

# convert this text to speech
text = "Yo, to the B, to the Ya"

engine.say(text)
# play the speech
engine.runAndWait()