import os
import webbrowser
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from datetime import datetime


# ==========================
# SPEAK FUNCTION
# ==========================

def speak(text):

    print(f"JARVIS: {text}")

    text = text.replace("'", "")

    os.system(
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        f'$speak.Speak(\'{text}\')"'
    )


# ==========================
# LISTEN FUNCTION
# ==========================

def listen():

    print("\nListening...")

    duration = 5
    samplerate = 48000

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        device=9
    )

    sd.wait()

    sf.write("voice.wav", recording, samplerate)

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile("voice.wav") as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text.lower()

    except Exception:
        return ""


# ==========================
# COMMANDS
# ==========================

def execute_command(command):

    if "open personal chrome" in command:

        speak("Opening personal chrome")

        os.system(
            'start chrome --profile-directory="Default"'
        )

    elif "open university chrome" in command:

        speak("Opening university chrome")

        os.system(
            'start chrome --profile-directory="Profile 1"'
        )

    elif "open private chrome" in command:

        speak("Opening private chrome")

        os.system(
            'start chrome --profile-directory="Profile 2"'
        )

    elif "open calculator" in command:

        speak("Opening calculator")

        os.system("calc")

    elif "open notepad" in command:

        speak("Opening notepad")

        os.system("notepad")

    elif "open paint" in command:

        speak("Opening paint")

        os.system("mspaint")

    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")

    elif "open gmail" in command:

        speak("Opening Gmail")

        webbrowser.open("https://mail.google.com")

    elif "open chat g p t" in command:

        speak("Opening Chat GPT")

        webbrowser.open("https://chatgpt.com")

    elif "search" in command:

        query = command.replace("search", "").strip()

        speak(f"Searching for {query}")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

    elif "time" in command:

        current_time = datetime.now().strftime("%I:%M %p")

        speak(f"The time is {current_time}")

    elif "stop" in command or "exit" in command:

        speak("See you soon Srija")

        return False

    elif command != "":

        speak("I do not know that command yet")

    return True


# ==========================
# MAIN PROGRAM
# ==========================

speak("Jarvis is ready")

running = True

while running:

    command = listen()

    if command == "":
        continue

    if not command.startswith("jarvis"):

        print("Wake word not detected")

        continue

    command = command.replace(
        "jarvis",
        "",
        1
    ).strip()

    if command == "":

        speak("Yes Srija")

        continue

    running = execute_command(command)