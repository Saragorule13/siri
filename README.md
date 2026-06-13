# Jackie - Local AI Desktop Assistant

Jackie is a local AI-powered desktop assistant that uses Large Language Models (LLMs) to understand natural language commands and perform desktop automation tasks. The assistant runs entirely on-device using Ollama and Faster-Whisper, providing a privacy-focused and offline-capable experience.

## Features

* Local LLM inference using Ollama
* AI-powered intent routing
* Voice command support using Faster-Whisper
* Desktop application launching
* Website opening through natural language commands
* Dynamic application registry
* Privacy-first, fully local execution
* Modular architecture for future expansion

## Tech Stack

### AI

* Ollama
* Qwen
* Faster-Whisper

### Backend

* Python

### Automation

* subprocess
* webbrowser

### Audio

* sounddevice
* scipy

## Installation

### Clone Repository

```bash
git clone https://github.com/Saragorule13/jackie.git
cd jackie
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama.

Pull the model:

```bash
ollama pull qwen3:8b
```

### Run Jackie

```bash
python main.py
```

## Example Commands

### Application Launching

```text
Open Chrome
Open Spotify
Open VS Code
Open Discord
```

### Website Launching

```text
Open GitHub
Open YouTube
Open LeetCode
```

### General Questions

```text
What is binary search?
Explain operating systems.
```

## Roadmap

### Completed

* [x] Local LLM Integration
* [x] AI Routing
* [x] Voice Input
* [x] Application Launcher
* [x] Website Launcher
* [x] Dynamic App Registry

### Planned

* [ ] Text-to-Speech (TTS)
* [ ] Memory System
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] Wake Word Detection
* [ ] Screen Understanding
* [ ] Plugin Architecture

## Why Jackie?

Most AI assistants rely heavily on cloud APIs. Jackie focuses on local inference and privacy while providing a foundation for building a fully capable desktop AI assistant.

## Author

**Sara Gorule**

GitHub: https://github.com/Saragorule13
