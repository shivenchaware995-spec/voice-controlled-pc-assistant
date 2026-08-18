# Voice Controlled PC Assistant

A Python-based voice assistant that allows you to control your Windows PC using voice commands.

## Features

* Voice command recognition
* Voice responses
* Google and YouTube search
* Open websites
* Open applications
* Open Desktop and Downloads
* Take screenshots
* Check CPU and RAM usage
* Open Calculator
* Open Notepad
* Tell the current time

## Technologies Used

* Python
* SpeechRecognition
* Pyttsx3
* PyAutoGUI
* Psutil
* PyAudio

## Project Structure

```text
voice-controlled-pc-assistant/
│
├── voice_assistant.py
├── README.md
└── screenshot.png
```

## Installation

Install the required Python libraries:

```bash
pip install SpeechRecognition pyttsx3 PyAudio pyautogui psutil
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/shivenchaware995-spec/voice-controlled-pc-assistant.git
```

Open the project folder:

```bash
cd voice-controlled-pc-assistant
```

Run the assistant:

```bash
python voice_assistant.py
```

## Voice Commands

You can use commands such as:

```text
Open Chrome
Open VS Code
Open YouTube
Search YouTube Python projects
Search Google Python tutorials
Open Downloads
Open Desktop
Take screenshot
System information
Open Calculator
Open Notepad
What is the time?
Exit
```

## How It Works

```text
Voice Input
     ↓
Speech Recognition
     ↓
Command Processing
     ↓
Command Matching
     ↓
PC Action
     ↓
Voice Response
```

The assistant listens to the user's voice, converts it into text, identifies the requested command, performs the corresponding action, and responds using text-to-speech.

## Future Improvements

* AI-based natural language understanding
* Voice-controlled file searching
* Screen text recognition
* More Windows controls
* Application management
* AI-powered error detection
* Custom wake word
* Offline voice recognition
* Personalized commands

## Author

Shiven Chaware

GitHub: https://github.com/shivenchaware995-spec
