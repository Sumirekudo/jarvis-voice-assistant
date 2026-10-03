import os

def speak(text):
    text = text.replace("'", "")
    os.system(
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        f'$speak.Speak(\'{text}\')"'
    )

speak("Hello")
speak("Goodbye")