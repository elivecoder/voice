import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()

def listen_and_process():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            window.update()
            audio = recognizer.listen(source, timeout=5)

            status_label.config(text="Processing...")
            window.update()

            # Convert speech to text
            command = recognizer.recognize_google(audio)
            display_command(command)
            respond(command)

    except sr.WaitTimeoutError:
        display_command("Timeout: No voice detected.")
    except sr.UnknownValueError:
        display_command("Sorry, I could not understand.")
    except sr.RequestError:
        display_command("Speech service is unavailable.")
    except Exception as e:
        display_command(f"Error: {str(e)}")

def display_command(command):
    command_label.config(text=f"You said: {command}")

def respond(command):
    # Basic responses (extend with more logic)
    response = ""
    command = command.lower()

    if "hello" in command:
        response = "Hello! How can I help you?"
    elif "your name" in command:
        response = "I am your Python voice assistant."
    elif "time" in command:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        response = f"The current time is {now}"
    else:
        response = "Sorry, I didn't understand that."

    speak(response)
    status_label.config(text=f"Response: {response}")

# GUI Setup
window = tk.Tk()
window.title("🎙️ Voice Assistant")
window.geometry("400x300")

title_label = tk.Label(window, text="Python Voice Assistant", font=("Helvetica", 16))
title_label.pack(pady=10)

command_label = tk.Label(window, text="Click the mic and speak", wraplength=350)
command_label.pack(pady=20)

mic_button = tk.Button(window, text="🎤 Speak", font=("Arial", 14), command=listen_and_process)
mic_button.pack(pady=10)

status_label = tk.Label(window, text="", fg="green")
status_label.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack(pady=10)

window.mainloop()
