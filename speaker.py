# python text_to_speech library imported
import pyttsx3

# programme for making computer to speak
if __name__=='__main__':
     # intialising module
    commander = pyttsx3.init()

    # Introduction done by commander, your personal speaker made by Amey Malpurkar
    commander.say ("Hi how are you I am Commander. your personal speaker what do you want me to speak for you my lord")
    commander.runAndWait()

    while True:
       
        # code for entering what you want to speak him for you
        speak_input = input("Enter here \n")

        # output
        commander.say(speak_input)
        commander.runAndWait()
        
