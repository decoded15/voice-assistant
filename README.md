# Voice Assistant

A voice assistant built using Faster-Whisper, Google Gemini, Edge-TTS, Streamlit, and Python.

This project enables natural voice-based interaction with an AI assistant capable of:

* capturing microphone input
* transcribing speech locally
* generating contextual AI responses
* maintaining conversational memory
* responding using natural voice synthesis

The project focuses heavily on real-world AI systems engineering concepts such as multimodal pipelines, conversational memory, streaming responses, audio processing, and modular AI orchestration.

---

# Features

* Microphone Audio Recording
* Local Speech-to-Text using Faster-Whisper
* Gemini-powered AI Conversations
* Conversational Memory System
* Personality-based AI Responses
* Neural Voice Output using Edge-TTS
* Streaming Text Rendering
* Streamlit Frontend Interface
* Modular AI Pipeline Architecture
* Persistent Conversation Loop

---

# Tech Stack

## Core

* Python
* Asyncio

## Speech-to-Text

* Faster-Whisper

## AI / LLM

* Google Gemini API

## Text-to-Speech

* Edge-TTS
* Playsound

## Frontend

* Streamlit

## Audio Processing

* SoundDevice
* SciPy

---

# System Architecture

```text
User Speech
      ↓
Audio Recording
      ↓
WAV Audio File
      ↓
Faster-Whisper
      ↓
Speech Transcript
      ↓
Gemini AI
      ↓
AI Response
      ↓
Edge-TTS
      ↓
Generated MP3
      ↓
Voice Playback
```

---

# Project Structure

```text
VOICE-ASSISTANT
│
├── audio
│   ├── recorder.py
│   ├── player.py
│   └── temp
│
├── stt
│   └── transcriber.py
│
├── llm
│   ├── gemini_engine.py
│   └── personality.py
│
├── tts
│   └── speaker.py
│
├── utils
│   └── config.py
│
├── app.py
├── .env
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/decoded15/voice-assistant.git

cd voice-assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Running the Project

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will run on:

```text
http://localhost:8501
```

---

# Conversational Workflow

```text
User Speaks
      ↓
Audio Recording
      ↓
Speech-to-Text
      ↓
Conversation Memory Injection
      ↓
Gemini Response Generation
      ↓
Streaming Text Rendering
      ↓
Neural Voice Synthesis
      ↓
Spoken AI Response
```

---

# Key AI Engineering Concepts Learned

* Speech-to-Text (STT)
* Text-to-Speech (TTS)
* Audio Pipelines
* Local AI Inference
* Multimodal AI Systems
* Conversational Memory
* Streaming Responses
* Event-driven Interaction
* Async Programming Fundamentals
* Prompt Engineering
* Personality Systems
* AI Orchestration Pipelines
* Frontend and Backend Integration
* State Management
* Cloud vs Local AI Systems

---

# Future Improvements

* Wake Word Detection
* Voice Activity Detection (VAD)
* Real-time Audio Streaming
* Ollama Integration
* Fully Local LLM Support
* Streaming TTS Playback
* Interruptible Conversations
* Persistent Long-term Memory
* Multiple AI Personalities
* Desktop Assistant Features
* FastAPI Backend Conversion

---

# Project Objective

This project was built to understand how modern conversational AI assistants are architected internally.

The focus was not only on building a working voice assistant, but also on learning:

* multimodal AI pipelines
* audio processing systems
* conversational memory architecture
* realtime interaction design
* streaming workflows
* AI orchestration patterns

---

# Author

Built by Dibyansh (decoded15)
