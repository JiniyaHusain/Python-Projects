import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker version 0.1 by Kaykobad : ")
    x = input("Enter what you want the system to speak: ")

    engine = pyttsx3.init()

    # Get the current speech rate
    rate = engine.getProperty('rate')
    

    # Set the speech rate to a slower speed (default is typically 200)
    engine.setProperty('rate', rate - 100)  # Decrease the rate by 50

    engine.say(x)
    engine.runAndWait()
