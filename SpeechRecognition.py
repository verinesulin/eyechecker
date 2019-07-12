#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
# import array
# Record Audio
# myArray = array.array('c', 'a\b')
# print(myArray[1])
i = 0
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
print(alphabet[0])
asd = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

# Speech recognition using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
    # instead of r.recognize_google(audio)
        asd = r.recognize_google(audio)
        print("You said: " + asd)
        if asd == "yes":
            print("you did it")
        if asd == alphabet[1]:
            i+=1
            print(i)
        # asd = ""
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    asd = ""

