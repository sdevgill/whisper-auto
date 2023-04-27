# Whisper Auto Transcription

A simple and easy-to-use audio transcription app that uses OpenAI's Whisper model
to transcribe audio files with your GPU, free of cost (except electricity!).

Tested on Windows 11 with an RTX 3090 and RTX 4090.

Important: Make sure you have the correct version of CUDA installed for your GPU. See this link for more information on properly installing whisper local to work with CUDA: <https://github.com/openai/whisper/discussions/47>

## Requirements

- Python 3.10.10

## Features

- Supports MP3, WAV, M4A and other common audio formats.
- Automatically transcribes all valid audio files in the input folder.
- Calculates the time each transcription took.
- Saves transcriptions and in separate text files in the output folder.

## Installation

1. Clone this repository and navigate to the project folder

```
git clone git@github.com:sdevgill/whisper-auto.git
cd whisper-auto
```

2. Create a virtual environment

```
python -m venv .venv
```

3. Activate the virtual environment (Poweshell)

```
.\.venv\Scripts\Activate.ps1
```

## Usage

1. Create an `.env` file in the project folder from the `.env.example` file

```
Copy-Item .env.example -Destination .env
```

2. Add your OpenAI API key to the `.env` file

```
OPENAI_API_KEY=YOUR_API_KEY
```

3. Create an `input` folder in the project folder and add your audio files to it

4. Run the app

```
python app.py
```
