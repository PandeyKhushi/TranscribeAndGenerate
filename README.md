# TranscribeAndGenerate
Automatic Speech Transcription and Generative AI Integration
## Overview
This project combines advanced AI technologies to create a system for speech transcription and text generation. Using Whisper, an automatic speech recognition (ASR) model, and Google Generative AI, the system transcribes spoken language into text and generates further content based on the transcription. The interface is built using Gradio, allowing users to interact easily with the system either through real-time speech input via a microphone or by uploading audio files. This solution is designed to make transcription and content generation more accessible and efficient, with potential use cases in content creation, accessibility tools, and interactive applications.
## Tools And Technologies Used
- Whisper (ASR Model): A pre-trained model from Hugging Face, used for automatic speech-to-text transcription. It handles real-time audio and pre-recorded audio files.

- Google Generative AI: After transcription, this model processes the text to generate further content based on a specified prompt. It includes configuration for creativity and safety filters to ensure that inappropriate content is blocked.

- Async Functions: The system uses asynchronous programming (via asyncio) to handle tasks efficiently, ensuring that transcription and text generation occur without delays.
## Future Scope 
- Multilingual Support: The system can be expanded to support multiple languages, allowing for a wider range of transcription and content generation capabilities.

- Text-to-Speech (TTS) Integration: Once the text is generated, it could be converted back into speech using tools like gTTS, making the solution accessible for those with visual impairments.

- Advanced User Control: Add more control over generative AI outputs, such as varying the creativity levels, adjusting output length, and providing feedback on generated content.

- Mobile App Integration: The system can be adapted into a mobile app, making it more portable and accessible for everyday use.

- Real-time Translation: Integrate real-time language translation, enabling users to transcribe and translate speech simultaneously.
 ## Dependencies
 ### FFmpeg
This project requires [FFmpeg](https://ffmpeg.org/download.html) to process audio files. 
### Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
## Installation
- On Windows: Download FFmpeg from the [official site](https://ffmpeg.org/download.html) and add it to your system's PATH.
- On Linux/Mac: Use your package manager:
  ```bash
  sudo apt install ffmpeg    # For Ubuntu/Debian
  brew install ffmpeg        # For macOS

### Install the required libraries:
```bash
pip install transformers gradio huggingface_hub gtts google-generativeai requests


 ## Output Screenshots
   
Output![Screenshot (49)](https://github.com/user-attachments/assets/9e1c75bc-15c4-42d6-938e-43955313871a)

  

